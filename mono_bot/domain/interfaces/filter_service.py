import abc
from typing import Iterable

from mono_bot.domain.dtos.account_dto import AccountDto
from mono_bot.domain.models.user_declaration import UserDeclaration


class IFilterService(abc.ABC):
    @abc.abstractmethod
    def filter_visible_accounts(self, uid: str, accounts: list[AccountDto]) -> Iterable[AccountDto]:
        """
        Filters accounts visible to the user with the given uid.
        """
        ...

    @abc.abstractmethod
    def filter_notification_targets(self, account: AccountDto) -> Iterable[UserDeclaration]:
        """
        Returns all user declarations that should be notified by the given account event.
        """
        ...
