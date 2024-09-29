from httpx import AsyncClient

from mono_bot.domain.config.config_service import ConfigService


def build_mono_client(config: ConfigService) -> AsyncClient:
    return AsyncClient(headers={
        'X-Token': config.mono_token,
    })
