from __future__ import annotations

from mono_bot.domain.dtos.account_dto import AccountDto


class AccountDeclaration:
    def __init__(self, iban: str | None, alias: str | None):
        self.iban = iban.strip().lower() if iban else None
        self.alias = alias

    @staticmethod
    def from_dict(data: dict) -> AccountDeclaration:
        return AccountDeclaration(
            iban=data.get('iban', None),
            alias=data.get('alias', None),
        )

    def __repr__(self) -> str:
        return f'AccountDeclaration(iban={self.iban}, alias={self.alias})'

    def matches_account(self, account: AccountDto) -> bool:
        return self.iban is None or account.iban.lower() == self.iban
