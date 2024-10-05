from __future__ import annotations

from typing import Iterable, Final

from mono_bot.domain.dtos.account_dto import AccountDto
from mono_bot.domain.dtos.webhook_dto import WebhookDto
from mono_bot.domain.interfaces.config_service import IConfigService
from mono_bot.domain.interfaces.presentation_service import IPresentationService
from mono_bot.domain.models.account_declaration import AccountDeclaration

_CODE_TO_CURRENCY: Final[dict[int, tuple[str, str]]] = {
    980: ('UAH', '₴'),
    840: ('USD', '$'),
    978: ('EUR', '€'),
    826: ('GBP', '£'),
    985: ('PLN', 'zl'),
}


class PresentationService(IPresentationService):
    def __init__(self, config: IConfigService):
        self.config = config

    def represent_accounts(self, accounts: Iterable[AccountDto]) -> str:
        return '\n'.join(map(self._represent_account, accounts))

    def represent_webhook(self, webhook: WebhookDto, account: AccountDto) -> str:
        item = webhook.statement_item

        return (f'**{item.float_amount} {self.represent_currency(item.currency_code)}**: '
                f'{item.description}\n'
                f'Balance: {item.float_balance} {self.represent_currency(account.currency_code)}')

    def represent_currency(self, currency_code: int) -> str:
        repr_ = _CODE_TO_CURRENCY.get(currency_code, None)

        if not repr_:
            return '???'

        return repr_[0]

    def _represent_account(self, account: AccountDto) -> str:
        return (f'{self._find_alias(account)}: **{account.float_balance} '
                f'{self.represent_currency(account.currency_code)}**')

    def _find_alias(self, account: AccountDto) -> str:
        declaration: AccountDeclaration | None = next(
            filter(lambda decl: decl.matches_account(account), self.config.account_declarations),
            None
        )

        if declaration and declaration.alias:
            return declaration.alias

        return account.iban
