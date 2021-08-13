from typing import Any, Dict, List, Optional, Union, overload, Tuple, SupportsInt


class Event:
    type: int
    __dict__: Dict[str, Any]
    __hash__: None  # type: ignore

    @overload
    def __init__(self, type: int, dict: Dict[str, Any]) -> None: ...

    @overload
    def __init__(self, type: int, **attributes: Any) -> None: ...

    def __getattr__(self, name: str) -> Any: ...


_EventTypes = Union[SupportsInt, Tuple[SupportsInt, ...], List[SupportsInt]]


def pump() -> None: ...


def get(eventtype: _EventTypes = None, pump: Any = True) -> List[Event]: ...


def poll() -> Event: ...


def wait(timeout: int = 0) -> Event: ...


def peek(eventtype: _EventTypes = None, pump: Any = True) -> bool: ...


def clear(eventtype: _EventTypes = None, pump: Any = True) -> None: ...


def event_name(type: int) -> str: ...


def set_blocked(type: Optional[_EventTypes]) -> None: ...


def set_allowed(type: Optional[_EventTypes]) -> None: ...


def get_blocked(type: _EventTypes) -> bool: ...


def set_grab(grab: bool) -> None: ...


def get_grab() -> bool: ...


def post(event: Event) -> bool: ...


def custom_type() -> int: ...
