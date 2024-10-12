import asyncio

from aiohttp import web
from dependency_injector.wiring import inject, Provide

from mono_bot.application.hook_server.webhook_controller import WebhookController
from mono_bot.domain.interfaces.config_service import IConfigService
from mono_bot.domain.interfaces.mono_repository import IMonoRepository


@inject
def build_server(config: IConfigService = Provide['config_service']) -> web.Application:
    app = web.Application()
    controller = WebhookController()

    app.add_routes([
        web.post(config.webhooks_server_endpoint, controller.receive_hook),
        web.get(config.webhooks_server_endpoint, controller.confirm_handshake),
    ])

    return app


@inject
async def webhooks_server_main(config: IConfigService = Provide['config_service'],
                               repository: IMonoRepository = Provide['mono_repository']):
    app = build_server()

    print(
        f'Starting webhooks server on '
        f'{config.webhooks_server_host}:{config.webhooks_server_port}'
        f'{config.webhooks_server_endpoint}'
    )

    # noinspection PyProtectedMember
    await asyncio.gather(
        web._run_app(app, host=config.webhooks_server_host, port=config.webhooks_server_port),
        repository.request_webhook(),
    )
