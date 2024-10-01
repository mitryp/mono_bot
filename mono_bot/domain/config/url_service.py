import yaml


class UrlService:
    def __init__(self, urls_file: str):
        with open(urls_file, 'r') as f:
            self.urls = yaml.safe_load(f)

    @property
    def client_info_endpoint(self):
        return self.urls['client_info']

    @property
    def webhook_endpoint(self):
        return self.urls['webhook']
