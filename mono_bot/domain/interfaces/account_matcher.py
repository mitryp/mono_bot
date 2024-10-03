import abc

from mono_bot.domain.dtos.account_dto import AccountDto


class IAccountMatcher(abc.ABC):
    @abc.abstractmethod
    def matches_account(self, account: AccountDto) -> bool:
        ...
