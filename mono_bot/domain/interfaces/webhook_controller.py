import abc

from aiohttp import web


class IWebhookController(abc.ABC):
    @abc.abstractmethod
    async def confirm_handshake(self, req: web.Request) -> web.Response:
        ...

    @abc.abstractmethod
    async def receive_hook(self, req: web.Request) -> web.Response:
        ...
