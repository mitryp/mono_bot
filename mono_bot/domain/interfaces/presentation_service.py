import abc
from typing import Iterable

from mono_bot.domain.dtos.account_dto import AccountDto
from mono_bot.domain.dtos.webhook_dto import WebhookDto


class IPresentationService(abc.ABC):
    @abc.abstractmethod
    def represent_currency(self, currency_code: int) -> str:
        ...

    @abc.abstractmethod
    def represent_webhook(self, webhook: WebhookDto, account: AccountDto) -> str:
        ...

    @abc.abstractmethod
    def represent_accounts(self, accounts: Iterable[AccountDto]) -> str:
        ...
