from dependency_injector.wiring import inject, Provide
from pyrogram import Client, filters
from pyrogram.types import Message

from mono_bot.domain.interfaces.config_service import IConfigService
from mono_bot.domain.interfaces.filter_service import IFilterService
from mono_bot.domain.interfaces.mono_repository import IMonoRepository
from mono_bot.domain.interfaces.presentation_service import IPresentationService


@inject
def build_tg_client(config: IConfigService = Provide['config_service'],
                    repository: IMonoRepository = Provide['mono_repository'],
                    filter_: IFilterService = Provide['filter_service'],
                    presenter: IPresentationService = Provide['presentation_service']) -> Client:
    client = Client(
        config.app_name,
        api_id=config.api_id,
        api_hash=config.api_hash,
        bot_token=config.bot_token
    )

    @client.on_message(filters.command('start') & filters.private & filters.user(config.whitelist_uids))
    async def start(_: Client, message: Message):
        await message.reply_text('Hi! Use /state command to get the info')

    @client.on_message(filters.command('state') & filters.private & filters.user(config.whitelist_uids))
    async def state(_: Client, message: Message):
        try:
            state_ = await repository.fetch_client_info()
        except KeyError:
            await message.reply_text('An error occurred during fetching client info. Please, try again later.')
            return

        visible_accounts = filter_.filter_visible_accounts(message.from_user.username, state_.accounts)

        if not visible_accounts:
            await message.reply_text('Your username is in the whitelist, but no visible accounts configured for you')
            return

        representation = presenter.represent_accounts(visible_accounts)

        await message.reply_text(representation)

    return client
