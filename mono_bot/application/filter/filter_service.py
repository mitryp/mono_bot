from typing import Callable

from mono_bot.domain.config.config_service import ConfigService
from mono_bot.domain.dtos.account_dto import AccountDto


class FilterService:
    def __init__(self, config: ConfigService):
        self.config = config

    def filter_accounts(self, accounts: list[AccountDto]) -> list[AccountDto]:
        if not self.config.visible_ibans:
            return accounts

        ibans = list(map(lambda x: x.lower(), self.config.visible_ibans))

        return filter(self._where_iban_in(ibans), accounts)

    @staticmethod
    def _where_iban_in(ibans: list[str]) -> Callable[[AccountDto], bool]:
        return lambda account: account.iban.lower() in ibans
