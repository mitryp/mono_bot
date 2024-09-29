from mono_bot.application.api.currency_code_service import CurrencyCodeService
from mono_bot.domain.dtos.account_dto import AccountDto


class RepresentationService:
    def __init__(self, currency_service: CurrencyCodeService):
        self.currency_service = currency_service

    def _represent_account(self, account: AccountDto) -> str:
        return (f'{account.iban}: **{account.float_balance} '
                f'{self.currency_service.represent_currency(account.currency_code)}**')

    def represent_accounts(self, accounts: list[AccountDto]) -> str:
        return '\n'.join(map(self._represent_account, accounts))
