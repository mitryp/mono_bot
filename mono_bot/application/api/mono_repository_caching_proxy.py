from __future__ import annotations

import time

from mono_bot.domain.dtos.client_info_dto import ClientInfoDto
from mono_bot.domain.interfaces.mono_repository import IMonoRepository


class MonoRepositoryCachingProxy(IMonoRepository):
    def __init__(self, repository: IMonoRepository, cache_lifetime_seconds: int = 60):
        self.repository: IMonoRepository = repository
        self.cache: ClientInfoDto | None = None
        self.last_cache_time: int | None = None
        self.cache_lifetime_seconds: int = cache_lifetime_seconds

    async def request_webhook(self):
        return await self.repository.request_webhook()

    async def fetch_client_info(self, read_cache=False) -> ClientInfoDto:
        now = time.time()

        if read_cache and self.cache:
            return self.cache

        if self.cache and self.last_cache_time and (now - self.last_cache_time) < self.cache_lifetime_seconds:
            return self.cache

        info = await self.repository.fetch_client_info()
        self.last_cache_time = time.time()
        self.cache = info

        return info
