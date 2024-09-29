from mono_bot.domain.dtos.account_dto import AccountDto


class ClientInfoDto:
    client_id: str
    name: str
    web_hook_url: str
    accounts: list[AccountDto]

    def __init__(self, client_id: str, name: str, web_hook_url: str, accounts: list[AccountDto]):
        self.client_id = client_id
        self.name = name
        self.web_hook_url = web_hook_url
        self.accounts = accounts

    @staticmethod
    def from_json(data: dict):
        return ClientInfoDto(
            client_id=data['clientId'],
            name=data['name'],
            web_hook_url=data['webHookUrl'],
            accounts=list(map(AccountDto.from_json, data['accounts'])),
        )

    def __repr__(self):
        return f'<ClientInfoDto: {self.name} {self.accounts}>'
