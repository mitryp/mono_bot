from __future__ import annotations

from typing import Iterable

from mono_bot.application.api.currency_code_service import CurrencyCodeService
from mono_bot.domain.config.config_service import ConfigService
from mono_bot.domain.dtos.account_dto import AccountDto
from mono_bot.domain.models.account_declaration import AccountDeclaration


class RepresentationService:
    def __init__(self, currency_service: CurrencyCodeService, config: ConfigService):
        self.currency_service = currency_service
        self.config = config

    def _represent_account(self, account: AccountDto) -> str:
        return (f'{self._find_alias(account)}: **{account.float_balance} '
                f'{self.currency_service.represent_currency(account.currency_code)}**')

    def _find_alias(self, account: AccountDto) -> str:
        declaration: AccountDeclaration | None = next(
            filter(lambda decl: decl.matches_account(account), self.config.account_declarations),
            None
        )

        if declaration and declaration.alias:
            return declaration.alias

        return account.iban

    def represent_accounts(self, accounts: Iterable[AccountDto]) -> str:
        return '\n'.join(map(self._represent_account, accounts))
