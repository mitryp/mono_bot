from __future__ import annotations

from typing import Callable, Iterable

from mono_bot.domain.config.config_service import ConfigService
from mono_bot.domain.dtos.account_dto import AccountDto
from mono_bot.domain.models.account_matcher import AccountMatcher
from mono_bot.domain.models.user_declaration import UserDeclaration


class FilterService:
    def __init__(self, config: ConfigService):
        self.config = config

    def filter_top_level_accounts(self, accounts: list[AccountDto]) -> Iterable[AccountDto]:
        return FilterService._filter_accounts(accounts, self.config.account_declarations)

    def filter_user_scope(self, uid: str, accounts: list[AccountDto]) -> Iterable[AccountDto]:
        # return FilterService._filter_accounts(accounts, self.config.whitelist)
        scope = self._find_user_scope(uid)

        if not scope:
            return []

        res: list[AccountDto] = list()
        for account in accounts:
            if account.iban.strip().lower() in scope.visible_ibans:
                res.append(account)

        return res

    def _find_user_scope(self, uid: str) -> UserDeclaration | None:
        for account in self.config.whitelist:
            if account.uid == uid:
                return account

    @staticmethod
    def _filter_accounts(accounts: Iterable[AccountDto], matchers: list[AccountMatcher]) -> Iterable[AccountDto]:
        if not matchers:
            return accounts

        return filter(FilterService._where_account_matches_any(matchers), accounts)

    @staticmethod
    def _where_account_matches_any(matchers: list[AccountMatcher]) -> Callable[[AccountDto], bool]:
        return lambda account: any(map(lambda declaration: declaration.matches_account(account), matchers))
