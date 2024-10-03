from __future__ import annotations

import yaml

from mono_bot.domain.interfaces.config_service import IConfigService
from mono_bot.domain.models.account_declaration import AccountDeclaration
from mono_bot.domain.models.user_declaration import UserDeclaration


class ConfigService(IConfigService):
    def __init__(self, config_file: str):
        with open(config_file, 'r') as f:
            self.config = yaml.safe_load(f)
        self._accounts_declarations: list[AccountDeclaration] | None = None

    @property
    def app_name(self) -> str:
        return 'MonoApi'

    @property
    def api_id(self) -> str:
        return self.config['api']['api_id']

    @property
    def api_hash(self) -> str:
        return self.config['api']['api_hash']

    @property
    def bot_token(self) -> str:
        return self.config['api']['bot_token']

    @property
    def whitelist(self) -> list[UserDeclaration]:
        return list(map(UserDeclaration.from_dict, self.config['whitelist']))

    @property
    def whitelist_uids(self) -> list[str]:
        return list(map(lambda x: x.uid, self.whitelist))

    @property
    def mono_token(self) -> str:
        return self.config['mono_token']

    @property
    def account_declarations(self) -> list[AccountDeclaration]:
        if self._accounts_declarations is not None:
            return self._accounts_declarations

        raw_ibans = self.config.get('account_aliases', [])
        parsed = list(map(AccountDeclaration.from_dict, raw_ibans))

        self._accounts_declarations = parsed

        return parsed

    @property
    def hooks_enabled(self) -> bool:
        return self.config['webhooks']['enabled']

    @property
    def webhooks_url(self) -> str:
        return self.config['webhooks']['url']

    @property
    def webhooks_server_host(self) -> str:
        return self.config['webhooks']['server']['host']

    @property
    def webhooks_server_port(self) -> int:
        return self.config['webhooks']['server']['port']

    @property
    def webhooks_server_endpoint(self) -> str:
        return self.config['webhooks']['server']['endpoint']
