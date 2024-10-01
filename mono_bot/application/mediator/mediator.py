from typing import Callable, Coroutine

from mono_bot.domain.models.async_event import AsyncEvent

Observer = Callable[[AsyncEvent], Coroutine]


class Mediator:
    def __init__(self):
        self.observers: list[Observer] = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    async def fire_event(self, event: AsyncEvent):
        for observer in self.observers:
            await observer(event)
