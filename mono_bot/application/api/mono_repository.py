import asyncio

from httpx import AsyncClient

from mono_bot.domain.dtos.client_info_dto import ClientInfoDto
from mono_bot.domain.interfaces.config_service import IConfigService
from mono_bot.domain.interfaces.mono_repository import IMonoRepository
from mono_bot.domain.interfaces.url_service import IUrlService


class MonoRepository(IMonoRepository):
    def __init__(self, client: AsyncClient, config_service: IConfigService, url_service: IUrlService):
        self.client = client
        self.config_service = config_service
        self.url_service = url_service

    async def fetch_client_info(self) -> ClientInfoDto:
        response = await self.client.get(self.url_service.client_info_endpoint)
        data = response.json()

        return ClientInfoDto.from_json(data)

    async def request_webhook(self):
        webhook_url = self.config_service.webhooks_url

        await asyncio.sleep(1)
        await self.client.post(
            self.url_service.webhook_endpoint,
            json={
                'webHookUrl': webhook_url
            }
        )
