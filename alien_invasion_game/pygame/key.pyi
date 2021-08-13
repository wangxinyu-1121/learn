from typing import Sequence, Optional, Tuple, Union, List
from typing_extensions import Protocol
from pygame.math import Vector2
from pygame.rect import Rect

_Coordinate = Union[Tuple[float, float], List[float], Vector2]
_CanBeRect = Union[
    Rect,
    Tuple[int, int, int, int], List[int],
    Tuple[_Coordinate, _Coordinate], List[_Coordinate]
]


class _HasRectAttribute(Protocol):
    rect: _CanBeRect


_RectValue = Union[
    _CanBeRect, _HasRectAttribute
]


def get_focused() -> bool: ...


def get_pressed() -> Sequence[bool]: ...


def get_mods() -> int: ...


def set_mods() -> int: ...


def set_repeat(delay: Optional[int] = 0, interval: Optional[int] = 0) -> None: ...


def get_repeat() -> Tuple[int, int]: ...


def name(key: int) -> str: ...


def key_code(name: str) -> int: ...


def start_text_input() -> None: ...


def stop_text_input() -> None: ...


def set_text_input_rect(_RectValue) -> None: ...
