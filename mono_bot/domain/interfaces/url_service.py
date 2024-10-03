import abc


class IUrlService(abc.ABC):
    @property
    @abc.abstractmethod
    def client_info_endpoint(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def webhook_endpoint(self) -> str:
        ...
