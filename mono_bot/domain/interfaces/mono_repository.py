import abc

from mono_bot.domain.dtos.client_info_dto import ClientInfoDto


class IMonoRepository(abc.ABC):
    @abc.abstractmethod
    async def fetch_client_info(self) -> ClientInfoDto:
        ...

    @abc.abstractmethod
    async def request_webhook(self, webhook_url: str):
        ...
