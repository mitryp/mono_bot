import asyncio
import os

from pyrogram import idle

from mono_bot.application.api.currency_code_service import CurrencyCodeService
from mono_bot.application.api.mono_client import build_mono_client
from mono_bot.application.api.mono_repository import MonoRepository
from mono_bot.application.bot.tg_client import build_tg_client
from mono_bot.application.filter.filter_service import FilterService
from mono_bot.application.represent.representation_service import RepresentationService
from mono_bot.domain.config.config_service import ConfigService
from mono_bot.domain.config.url_service import UrlService


async def main():
    script_path = os.path.dirname(__file__)
    config_file = os.path.join(script_path, 'config.yaml')
    url_file = os.path.join(script_path, 'urls.yaml')

    config = ConfigService(config_file)
    url_service = UrlService(url_file)

    client = build_mono_client(config)
    repository = MonoRepository(client, url_service)
    filter_service = FilterService(config)
    currency_service = CurrencyCodeService()
    repr_service = RepresentationService(currency_service, config)

    print(config.whitelist)

    tg_client = await build_tg_client(config, repository, filter_service, repr_service)
    await tg_client.start()
    await idle()


if __name__ == '__main__':
    asyncio.run(main())
