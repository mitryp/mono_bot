from pyrogram import Client, filters
from pyrogram.types import Message

from mono_bot.application.api.mono_repository import MonoRepository
from mono_bot.application.filter.filter_service import FilterService
from mono_bot.application.represent.representation_service import RepresentationService
from mono_bot.domain.config.config_service import ConfigService


def build_tg_client(config: ConfigService, repository: MonoRepository, filter_service: FilterService,
                    repr_service: RepresentationService) -> Client:
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
            _state = await repository.fetch_client_info()
        except KeyError:
            await message.reply_text('An error occurred during fetching client info. Please, try again later.')
            return

        visible_accounts = filter_service.filter_user_scope(message.from_user.username, _state.accounts)

        if not visible_accounts:
            await message.reply_text('Your username is in the whitelist, but no visible accounts configured for you')
            return

        representation = repr_service.represent_accounts(visible_accounts)

        await message.reply_text(representation)

    return client
