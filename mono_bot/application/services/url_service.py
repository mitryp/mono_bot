import yaml

from mono_bot.domain.interfaces.url_service import IUrlService


class UrlService(IUrlService):
    def __init__(self, urls_file: str):
        with open(urls_file, 'r') as f:
            self.urls = yaml.safe_load(f)

    @property
    def client_info_endpoint(self) -> str:
        return self.urls['client_info']

    @property
    def webhook_endpoint(self) -> str:
        return self.urls['webhook']
