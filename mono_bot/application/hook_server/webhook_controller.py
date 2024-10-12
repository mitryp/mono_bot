from aiohttp import web
from dependency_injector.wiring import inject, Provide

from mono_bot.application.mediator.mediator import Mediator
from mono_bot.domain.dtos.webhook_dto import WebhookDto
from mono_bot.domain.interfaces.webhook_controller import IWebhookController
from mono_bot.domain.models.async_event import AsyncEvent


class WebhookController(IWebhookController):
    @inject
    async def confirm_handshake(self, req: web.Request,
                                mediator: Mediator = Provide['mediator']) -> web.Response:
        await mediator.fire_event(AsyncEvent(event_type=AsyncEvent.HANDSHAKE))

        return web.Response()

    @inject
    async def receive_hook(self, request: web.Request, mediator: Mediator = Provide['mediator']) -> web.Response:
        json = await request.json()

        try:
            hook_dto = WebhookDto.from_json(json)
            await mediator.fire_event(AsyncEvent(event_type=AsyncEvent.HOOK_TRIGGERRED, data=hook_dto))
        except KeyError:
            await mediator.fire_event(AsyncEvent(event_type=AsyncEvent.HOOK_FAILED))

        return web.Response()
