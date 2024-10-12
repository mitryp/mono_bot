from dependency_injector.wiring import inject, Provide
from pyrogram import Client

from mono_bot.domain.abs.message_service import MessageServiceBase
from mono_bot.domain.interfaces.config_service import IConfigService


@inject
def build_tg_client(config: IConfigService = Provide['config_service'],
                    message_service: MessageServiceBase = Provide['message_service']) -> Client:
    client = Client(
        config.app_name,
        api_id=config.api_id,
        api_hash=config.api_hash,
        bot_token=config.bot_token
    )

    client.add_handler(message_service.start_command)
    client.add_handler(message_service.state_command)

    return client
