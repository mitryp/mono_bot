import asyncio

from dependency_injector import providers

from mono_bot.application.api.mono_repository import MonoRepository
from mono_bot.application.api.mono_repository_caching_proxy import MonoRepositoryCachingProxy
from mono_bot.application.bot.bot_thread import bot_main
from mono_bot.application.di.containers import Container
from mono_bot.application.hook_server.server import webhooks_server_main
from mono_bot.domain.interfaces.config_service import IConfigService


async def main():
    container = Container()
    container.mono_repository.override(
        providers.Singleton(
            MonoRepositoryCachingProxy,
            repository=providers.Factory(
                MonoRepository,
                container.http_client,
                container.config_service,
                container.url_service,
            )
        )
    )

    config: IConfigService = container.config_service()

    futures = [bot_main()]
    if config.hooks_enabled:
        futures.append(webhooks_server_main())

    await asyncio.gather(*futures)


if __name__ == '__main__':
    asyncio.run(main())
