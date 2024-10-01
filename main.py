import asyncio
import os

from mono_bot.application.bot.bot_thread import bot_main
from mono_bot.application.mediator.mediator import Mediator
from mono_bot.application.hook_server.server import webhooks_server
from mono_bot.domain.config.config_service import ConfigService
from mono_bot.domain.config.url_service import UrlService


async def main():
    script_path = os.path.dirname(__file__)
    config_file = os.path.join(script_path, 'config.yaml')
    url_file = os.path.join(script_path, 'urls.yaml')

    config = ConfigService(config_file)
    url_service = UrlService(url_file)
    print('hooks', config.hooks_enabled)
    mediator = Mediator()

    futures = [bot_main(config, url_service, mediator)]
    if config.hooks_enabled:
        futures.append(webhooks_server(config, mediator))

    await asyncio.gather(*futures)


if __name__ == '__main__':
    asyncio.run(main())
