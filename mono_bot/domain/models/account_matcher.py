from mono_bot.domain.dtos.account_dto import AccountDto


class AccountMatcher:
    def matches_account(self, account: AccountDto) -> bool:
        raise NotImplementedError
