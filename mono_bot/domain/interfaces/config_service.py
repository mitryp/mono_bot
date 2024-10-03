import abc

from mono_bot.domain.models.account_declaration import AccountDeclaration
from mono_bot.domain.models.user_declaration import UserDeclaration


class IConfigService(abc.ABC):
    @property
    @abc.abstractmethod
    def app_name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def api_id(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def api_hash(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def bot_token(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def whitelist(self) -> list[UserDeclaration]:
        ...

    @property
    @abc.abstractmethod
    def whitelist_uids(self) -> list[str]:
        ...

    @property
    @abc.abstractmethod
    def mono_token(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def account_declarations(self) -> list[AccountDeclaration]:
        ...

    @property
    @abc.abstractmethod
    def hooks_enabled(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def webhooks_url(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def webhooks_server_host(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def webhooks_server_port(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def webhooks_server_endpoint(self) -> str:
        ...
