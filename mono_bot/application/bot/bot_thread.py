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
from mono_bot.domain.models.async_event import AsyncEvent


async def bot_main(mediator: Mediator):
    script_path = os.path.dirname(sys.argv[0])
    config_file = os.path.join(script_path, 'config.yaml')
    url_file = os.path.join(script_path, 'urls.yaml')

    config = ConfigService(config_file)
    url_service = UrlService(url_file)

    client = build_mono_client(config)
    repository = MonoRepository(client, url_service)
    filter_service = FilterService(config)
    currency_service = CurrencyCodeService()
    repr_service = RepresentationService(currency_service, config)

    tg_client = build_tg_client(config, repository, filter_service, repr_service)

    mediator.add_observer(lambda x: on_event(tg_client, x))

    await tg_client.start()
    await idle()


async def on_event(client: Client, event: AsyncEvent):
    await client.send_message('mitryp', f'```json\n'
                                        f'{event.data}```')
