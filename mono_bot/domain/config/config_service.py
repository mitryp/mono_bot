import yaml


class ConfigService:
    def __init__(self, config_file: str):
        with open(config_file, 'r') as f:
            self.config = yaml.safe_load(f)

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
    def whitelist(self) -> str:
        return self.config['whitelist']

    @property
    def mono_token(self) -> str:
        return self.config['mono_token']

    @property
    def visible_ibans(self) -> list[str]:
        return self.config.get('visible_ibans', [])
