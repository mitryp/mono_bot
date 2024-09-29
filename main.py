import asyncio
import os

from mono_bot.application.api.client import build_client
from mono_bot.application.api.mono_repository import MonoRepository
from mono_bot.domain.config.config_service import ConfigService
from mono_bot.domain.config.url_service import UrlService


async def main():
    script_path = os.path.dirname(__file__)
    config_file = os.path.join(script_path, 'config.yaml')
    url_file = os.path.join(script_path, 'urls.yaml')

    config = ConfigService(config_file)
    url_service = UrlService(url_file)

    client = build_client(config)
    repository = MonoRepository(client, url_service)

    res = await repository.fetch_client_info()
    print(res)


if __name__ == '__main__':
    asyncio.run(main())
