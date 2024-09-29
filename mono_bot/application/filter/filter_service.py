from typing import Callable, Iterable

from mono_bot.domain.config.config_service import ConfigService
from mono_bot.domain.dtos.account_dto import AccountDto
from mono_bot.domain.models.account_declaration import AccountDeclaration


class FilterService:
    def __init__(self, config: ConfigService):
        self.config = config

    def filter_accounts(self, accounts: list[AccountDto]) -> Iterable[AccountDto]:
        declarations = self.config.account_declarations

        if not declarations:
            return accounts

        return filter(self._where_account_declared_in(declarations), accounts)

    @staticmethod
    def _where_account_declared_in(declarations: list[AccountDeclaration]) -> Callable[[AccountDto], bool]:
        return lambda account: any(map(lambda declaration: declaration.matches_account(account), declarations))
