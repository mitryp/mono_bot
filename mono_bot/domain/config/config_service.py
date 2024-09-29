import yaml


class ConfigService:
    def __init__(self, config_file: str):
        with open(config_file, 'r') as f:
            self.config = yaml.safe_load(f)

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
    def whitelisted_numbers(self):
        return self.config['whitelist']

    @property
    def mono_token(self):
        return self.config['mono_token']
