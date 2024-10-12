import abc

from pyrogram import Client, filters
from pyrogram.filters import Filter
from pyrogram.handlers import MessageHandler
from pyrogram.handlers.handler import Handler
from pyrogram.types import Message


class MessageServiceBase(abc.ABC):
    @abc.abstractmethod
    def build_base_filters(self) -> Filter:
        ...

    @abc.abstractmethod
    async def on_start_command(self, client: Client, message: Message) -> None:
        ...

    @abc.abstractmethod
    async def on_state_command(self, client: Client, message: Message) -> None:
        ...

    @property
    def start_command(self) -> Handler:
        return MessageHandler(self.on_start_command, filters.command('start') & self.build_base_filters())

    @property
    def state_command(self) -> Handler:
        return MessageHandler(self.on_state_command, filters.command('state') & self.build_base_filters())
