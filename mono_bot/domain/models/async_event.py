from __future__ import annotations

from typing import Any


class AsyncEvent:
    def __init__(self, event_type: str, data: Any | None):
        self.event_type = event_type
        self.data = data
