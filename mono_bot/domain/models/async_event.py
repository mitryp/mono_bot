from __future__ import annotations

from typing import Any


class AsyncEvent:
    HOOK_TRIGGERRED = 'hook_triggered'
    HOOK_FAILED = 'hook_failed'
    HANDSHAKE = 'handshake'

    def __init__(self, event_type: str, data: Any | None = None):
        self.event_type = event_type
        self.data = data

    def __repr__(self):
        return f'<AsyncEvent {self.event_type} {self.data}>'
