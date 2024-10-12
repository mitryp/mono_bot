from dependency_injector.wiring import inject, Provide
from httpx import AsyncClient

from mono_bot.domain.interfaces.config_service import IConfigService


@inject
def build_mono_client(config: IConfigService = Provide['config_service']) -> AsyncClient:
    return AsyncClient(headers={
        'X-Token': config.mono_token,
    })
