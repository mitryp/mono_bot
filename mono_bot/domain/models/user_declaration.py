from __future__ import annotations

from mono_bot.domain.dtos.account_dto import AccountDto
from mono_bot.domain.interfaces.account_matcher import IAccountMatcher


class UserDeclaration(IAccountMatcher):
    def __init__(self, uid: str, visible_ibans: list[str] | None, notify: bool):
        self.uid = uid
        self.visible_ibans = visible_ibans or []
        self.notify = notify

    @staticmethod
    def from_dict(data: dict) -> UserDeclaration:
        visible_ibans: list[str] | None = data.get('visible_ibans', None)

        return UserDeclaration(
            uid=data['uid'],
            visible_ibans=list(map(lambda x: x.strip().lower(), visible_ibans)) if visible_ibans else None,
            notify=data.get('notify', False),
        )

    def __repr__(self) -> str:
        return f'UserDeclaration(uid={self.uid}, visible_ibans={self.visible_ibans}, notify={self.notify})'

    def matches_account(self, account: AccountDto) -> bool:
        return account.iban.strip().lower() in self.visible_ibans
