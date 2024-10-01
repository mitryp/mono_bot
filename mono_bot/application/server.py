from aiohttp import web

from mono_bot.application.mediator.mediator import Mediator
from mono_bot.domain.models.async_event import AsyncEvent


async def receive_hook(request: web.Request, mediator: Mediator) -> web.Response:
    json = await request.json()
    await mediator.fire_event(AsyncEvent(event_type='hook_triggered', data=json))

    return web.Response()


def build_server(mediator: Mediator) -> web.Application:
    app = web.Application()
    app.add_routes([
        web.post(
            '/hook',
            lambda req: receive_hook(req, mediator)
        ),
    ])

    return app


async def run_server(mediator: Mediator):
    app = build_server(mediator)
    await web._run_app(app, host='localhost', port=8080)
