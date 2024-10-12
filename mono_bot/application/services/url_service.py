import yaml

from mono_bot.domain.interfaces.url_service import IUrlService


class UrlService(IUrlService):
    def __init__(self, urls: dict):
        self.urls = urls

    @staticmethod
    def from_file(urls_file: str) -> 'UrlService':
        with open(urls_file, 'r') as f:
            urls = yaml.safe_load(f)

        return UrlService(urls)

    @property
    def client_info_endpoint(self) -> str:
        return self.urls['client_info']

    @property
    def webhook_endpoint(self) -> str:
        return self.urls['webhook']
