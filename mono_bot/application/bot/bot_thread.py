import asyncio
import os
import sys

from pyrogram import idle, Client

from mono_bot.application.api.currency_code_service import CurrencyCodeService
from mono_bot.application.api.mono_client import build_mono_client
from mono_bot.application.api.mono_repository import MonoRepository
from mono_bot.application.bot.tg_client import build_tg_client
from mono_bot.application.filter.filter_service import FilterService
from mono_bot.application.mediator.mediator import Mediator
from mono_bot.application.represent.representation_service import RepresentationService
from mono_bot.domain.config.config_service import ConfigService
from mono_bot.domain.config.url_service import UrlService
from mono_bot.domain.dtos.webhook_dto import WebhookDto
from mono_bot.domain.models.async_event import AsyncEvent


async def bot_main(config: ConfigService, url_service: UrlService, mediator: Mediator):
    client = build_mono_client(config)
    repository = MonoRepository(client, url_service)
    filter_service = FilterService(config)
    currency_service = CurrencyCodeService()
    repr_service = RepresentationService(currency_service, config)

    tg_client = build_tg_client(config, repository, filter_service, repr_service)

    mediator.add_observer(lambda x: on_event(x, tg_client, repr_service))

    print('Starting the bot')

    await tg_client.start()

    futures = [idle()]
    # if config.hooks_enabled:
    #     futures.append(repository.request_webhook(config.webhooks_url))

    await asyncio.gather(*futures)


async def on_event(event: AsyncEvent, client: Client, repr_service: RepresentationService):
    if event.event_type != AsyncEvent.HOOK_TRIGGERRED:
        print(event)
        return

    dto: WebhookDto = event.data
    print(dto)

    await client.send_message('mitryp', repr_service.represent_webhook(dto))
