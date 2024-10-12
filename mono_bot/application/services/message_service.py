from dependency_injector.wiring import Provide, inject
from pyrogram import filters, Client
from pyrogram.filters import Filter
from pyrogram.types import Message

from mono_bot.domain.abs.message_service import MessageServiceBase
from mono_bot.domain.interfaces.config_service import IConfigService
from mono_bot.domain.interfaces.filter_service import IFilterService
from mono_bot.domain.interfaces.mono_repository import IMonoRepository
from mono_bot.domain.interfaces.presentation_service import IPresentationService


class MessageService(MessageServiceBase):
    @inject
    def build_base_filters(self, config_service: IConfigService = Provide['config_service']) -> Filter:
        return filters.private & filters.user(config_service.whitelist_uids)

    async def on_start_command(self, client: Client, message: Message) -> None:
        await message.reply_text('Hi! Use /state command to get the info')

    @inject
    async def on_state_command(self, client: Client, message: Message,
                               repository: IMonoRepository = Provide['mono_repository'],
                               filter_: IFilterService = Provide['filter_service'],
                               presenter: IPresentationService = Provide['presentation_service']) -> None:
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
