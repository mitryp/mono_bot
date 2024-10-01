import asyncio

from httpx import AsyncClient

from mono_bot.domain.config.url_service import UrlService
from mono_bot.domain.dtos.client_info_dto import ClientInfoDto


class MonoRepository:
    def __init__(self, client: AsyncClient, url_service: UrlService):
        self.client = client
        self.url_service = url_service

    async def fetch_client_info(self) -> ClientInfoDto:
        response = await self.client.get(self.url_service.client_info_endpoint)
        data = response.json()

        return ClientInfoDto.from_json(data)

    async def request_webhook(self, webhook_url: str):
        await asyncio.sleep(1)
        await self.client.post(
            self.url_service.webhook_endpoint,
            json={
                'webHookUrl': webhook_url
            }
        )
