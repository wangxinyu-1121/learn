from typing import Union, Tuple, List, Optional, Dict, Sequence
from typing_extensions import Protocol

from pygame.color import Color
from pygame.surface import Surface
from pygame.rect import Rect
from pygame.math import Vector2
from pygame.constants import FULLSCREEN

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
_ColorValue = Union[
    Color, int, Tuple[int, int, int], Tuple[int, int, int, int], List[int]
]


class _VidInfo:
    hw: int
    wm: int
    video_mem: int
    bitsize: int
    bytesize: int
    masks: Tuple[int, int, int, int]
    shifts: Tuple[int, int, int, int]
    losses: Tuple[int, int, int, int]
    blit_hw: int
    blit_hw_CC: int
    blit_hw_A: int
    blit_sw: int
    blit_sw_CC: int
    blit_sw_A: int
    current_h: int
    current_w: int


def init() -> None: ...


def quit() -> None: ...


def get_init() -> bool: ...


def set_mode(
        size: Optional[Union[Tuple[int, int], Sequence[int]]],
        flags: Optional[int] = 0,
        depth: Optional[int] = 0,
        display: Optional[int] = 0,
        vsync: Optional[int] = 0
) -> Surface: ...


def get_surface() -> Surface: ...


def flip() -> None: ...


def update(rectangle: Optional[Union[_RectValue, List[_RectValue]]] = None) -> None: ...


def get_driver() -> str: ...


def Info() -> _VidInfo: ...


def get_wm_info() -> Dict[str, int]: ...


def list_modes(
        depth: Optional[int] = 0,
        flags: Optional[int] = FULLSCREEN,
        display: Optional[int] = 0,
) -> List[Tuple[int, int]]: ...


def mode_ok(
        size: Union[Sequence[int], Tuple[int, int]],
        flags: Optional[int] = 0,
        depth: Optional[int] = 0,
        display: Optional[int] = 0,
) -> int: ...


def gl_get_attribute(flag: int) -> int: ...


def gl_set_attribute(flag: int, value: int) -> None: ...


def get_active() -> int: ...


def iconify() -> int: ...


def toggle_fullscreen() -> int: ...


def set_gamma(
        red: float, green: Optional[float] = None, blue: Optional[float] = None
) -> int: ...


def set_gamma_ramp(
        red: Sequence[int], green: Sequence[int], blue: Sequence[int]
) -> int: ...


def set_icon(surface: Surface) -> None: ...


def set_caption(title: str, icontitle: Optional[str] = None) -> None: ...


def get_caption() -> Tuple[str, str]: ...


def set_palette(palette: Sequence[_ColorValue]) -> None: ...


def get_num_displays() -> int: ...


def get_window_size() -> Tuple[int, int]: ...


def get_allow_screensaver() -> bool: ...


def set_allow_screensaver(value: bool) -> None: ...
