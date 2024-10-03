from __future__ import annotations

from typing import Iterable, Callable

from mono_bot.domain.dtos.account_dto import AccountDto
from mono_bot.domain.interfaces.account_matcher import IAccountMatcher
from mono_bot.domain.interfaces.config_service import IConfigService
from mono_bot.domain.interfaces.filter_service import IFilterService
from mono_bot.domain.models.user_declaration import UserDeclaration


class FilterService(IFilterService):
    def __init__(self, config: IConfigService):
        self.config = config

    def filter_notification_targets(self, account: AccountDto) -> Iterable[UserDeclaration]:
        return filter(lambda user: user.notify and user.matches_account(account), self.config.whitelist)

    def filter_visible_accounts(self, uid: str, accounts: list[AccountDto]) -> Iterable[AccountDto]:
        scope = self._find_user_scope(uid)

        if not scope:
            return []

        res: list[AccountDto] = list()
        for account in accounts:
            if account.iban.strip().lower() in scope.visible_ibans:
                res.append(account)

        return res

    def _find_user_scope(self, uid: str) -> UserDeclaration | None:
        return next(filter(lambda acc: acc.uid == uid, self.config.whitelist), None)

    @staticmethod
    def _filter_accounts(accounts: Iterable[AccountDto], matchers: list[IAccountMatcher]) -> Iterable[AccountDto]:
        if not matchers:
            return accounts

        return filter(FilterService._where_account_matches_any(matchers), accounts)

    @staticmethod
    def _where_account_matches_any(matchers: list[IAccountMatcher]) -> Callable[[AccountDto], bool]:
        return lambda account: any(map(lambda declaration: declaration.matches_account(account), matchers))
