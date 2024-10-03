from aiohttp import web

from mono_bot.application.hook_server.webhook_controller import WebhookController
from mono_bot.application.mediator.mediator import Mediator
from mono_bot.application.services.config_service import ConfigService


# async def confirm_handshake(_: web.Request, mediator: Mediator) -> web.Response:
#     await mediator.fire_event(AsyncEvent(event_type=AsyncEvent.HANDSHAKE))
#
#     return web.Response()
#
#
# async def receive_hook(request: web.Request, mediator: Mediator) -> web.Response:
#     json = await request.json()
#
#     try:
#         hook_dto = WebhookDto.from_json(json)
#         await mediator.fire_event(AsyncEvent(event_type=AsyncEvent.HOOK_TRIGGERRED, data=hook_dto))
#     except KeyError:
#         await mediator.fire_event(AsyncEvent(event_type=AsyncEvent.HOOK_FAILED))
#
#     return web.Response()


def build_server(config: ConfigService, mediator: Mediator) -> web.Application:
    app = web.Application()
    controller = WebhookController(mediator)

    app.add_routes([
        web.post(config.webhooks_server_endpoint, controller.receive_hook),
        web.get(config.webhooks_server_endpoint, controller.confirm_handshake),
    ])

    return app


async def webhooks_server_main(config: ConfigService, mediator: Mediator):
    app = build_server(config, mediator)

    print(
        f'Starting webhooks server on '
        f'{config.webhooks_server_host}:{config.webhooks_server_port}'
        f'{config.webhooks_server_endpoint}'
    )

    # noinspection PyProtectedMember
    await web._run_app(app, host=config.webhooks_server_host, port=config.webhooks_server_port)
