from typing import List, Optional, Union, Tuple, IO, Hashable, Iterable

if sys.version_info >= (3, 6):
    from os import PathLike

    AnyPath = Union[str, bytes, PathLike[str], PathLike[bytes]]
else:
    AnyPath = Union[Text, bytes]

from pygame.color import Color
from pygame.surface import Surface

_ColorValue = Union[
    Color, Tuple[int, int, int], List[int], int, Tuple[int, int, int, int]
]


def init() -> None: ...


def quit() -> None: ...


def get_init() -> bool: ...


def get_default_font() -> str: ...


def get_fonts() -> List[str]: ...


def match_font(
        name: Union[str, bytes, Iterable[Union[str, bytes]]],
        bold: Optional[Hashable] = False,
        italic: Optional[Hashable] = False
) -> str: ...


def SysFont(
        name: Union[str, bytes, Iterable[Union[str, bytes]]],
        size: int,
        bold: Optional[Hashable] = False,
        italic: Optional[Hashable] = False,
) -> Font: ...


class Font(object):
    bold: bool
    italic: bool
    underline: bool

    def __init__(self, name: Union[AnyPath, IO, None], size: int) -> None: ...

    def render(
            self,
            text: str,
            antialias: bool,
            color: _ColorValue,
            background: Optional[_ColorValue] = None,
    ) -> Surface: ...

    def size(self, text: str) -> Tuple[int, int]: ...

    def set_underline(self, value: bool) -> None: ...

    def get_underline(self) -> bool: ...

    def set_bold(self, value: bool) -> None: ...

    def get_bold(self) -> bool: ...

    def set_italic(self, value: bool) -> None: ...

    def metrics(self, text: str) -> List[Tuple[int, int, int, int, int]]: ...

    def get_italic(self) -> bool: ...

    def get_linesize(self) -> int: ...

    def get_height(self) -> int: ...

    def get_ascent(self) -> int: ...

    def get_descent(self) -> int: ...
