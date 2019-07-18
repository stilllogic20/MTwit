from enum import Enum, auto
from typing import Any, Callable, List


class NotificationKind(Enum):
    FAVORITE = auto()
    RETWEET = auto()
    ERROR = auto()
    UNKNOWN = auto()


_handlers: List[Callable[[NotificationKind, str], Any]] = []


def subscribe(handler: Callable[[NotificationKind, str], Any]):
    _handlers.append(handler)


def unsubscribe(handler: Callable[[NotificationKind, str], Any]):
    _handlers.remove()


def observe(handler):
    subscribe(handler)
    return handler


def notify(kind: NotificationKind, details: str = ""):
    for handler in _handlers:
        handler(kind, details)
