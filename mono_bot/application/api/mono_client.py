from httpx import AsyncClient

from mono_bot.domain.interfaces.config_service import IConfigService


def build_mono_client(config: IConfigService) -> AsyncClient:
    return AsyncClient(headers={
        'X-Token': config.mono_token,
    })
