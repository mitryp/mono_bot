import asyncio

from dependency_injector.wiring import inject, Provide
from pyrogram import idle, Client
from pyrogram.types import BotCommand

from mono_bot.application.api.mono_repository_caching_proxy import MonoRepositoryCachingProxy
from mono_bot.application.mediator.mediator import Mediator
from mono_bot.domain.dtos.webhook_dto import WebhookDto
from mono_bot.domain.interfaces.config_service import IConfigService
from mono_bot.domain.interfaces.filter_service import IFilterService
from mono_bot.domain.interfaces.mono_repository import IMonoRepository
from mono_bot.domain.interfaces.presentation_service import IPresentationService
from mono_bot.domain.models.async_event import AsyncEvent


@inject
async def bot_main(
        tg_client: Client = Provide['tg_client'],
        config: IConfigService = Provide['config_service'],
        mediator: Mediator = Provide['mediator']):
    print('Starting the bot')

    await tg_client.start()
    await tg_client.set_bot_commands([
        BotCommand('state', 'Get the current state of the accounts visible to you'),
    ])

    futures = [idle()]
    if config.hooks_enabled:
        mediator.add_observer(on_event)

    await asyncio.gather(*futures)


@inject
async def on_event(event: AsyncEvent,
                   client: Client = Provide['tg_client'],
                   repo: IMonoRepository = Provide['mono_repository'],
                   presenter: IPresentationService = Provide['presentation_service'],
                   filter_: IFilterService = Provide['filter_service']):
    if event.event_type != AsyncEvent.HOOK_TRIGGERRED:
        print(event)
        return

    dto: WebhookDto = event.data

    if type(repo) is MonoRepositoryCachingProxy:
        # noinspection PyTypeChecker
        proxy: MonoRepositoryCachingProxy = repo
        client_info = await proxy.fetch_client_info(read_cache=True)
    else:
        client_info = await repo.fetch_client_info()

    target_account = next(filter(lambda acc: acc.id == dto.account_id, client_info.accounts), None)

    if target_account is None:
        print(f'Could not find account {dto.account_id}')
        return

    target_users = filter_.filter_notification_targets(target_account)

    if not target_users:
        print(f'No users scoped for account {dto.account_id}')
        return

    message = presenter.represent_webhook(dto, target_account)

    for user in target_users:
        print(f'Notifying user {user.uid}')
        await client.send_message(user.uid, message)
