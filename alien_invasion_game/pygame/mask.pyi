from typing import Optional, Union, Text, Tuple, List, TypeVar, Sequence
from typing_extensions import Protocol

from pygame.math import Vector2
from pygame.surface import Surface
from pygame.rect import Rect
from pygame.color import Color

_ColorValue = Union[
    Color, Tuple[int, int, int], List[int], int, Tuple[int, int, int, int]
]
_ToSurfaceColorValue = Union[
    Color, Tuple[int, int, int], List[int], int, Text, Tuple[int, int, int, int]
]
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
_Offset = TypeVar("_Offset", Tuple[int, int], Sequence[int])


def from_surface(surface: Surface, threshold: Optional[int] = 127) -> Mask: ...


def from_threshold(
        surface: Surface,
        color: _ColorValue,
        threshold: Optional[_ColorValue] = (0, 0, 0, 255),
        other_surface: Optional[Surface] = None,
        palette_colors: Optional[int] = 1,
) -> Mask: ...


class Mask:
    def __init__(
            self, size: Union[List[int], Tuple[int, int]], fill: Optional[bool] = False
    ) -> None: ...

    def copy(self) -> Mask: ...

    def get_size(self) -> Tuple[int, int]: ...

    def get_rect(self, **kwargs) -> Rect: ...  # Dict type needs to be completed

    def get_at(self, pos: Union[List[int], Tuple[int, int]]) -> int: ...

    def set_at(
            self, pos: Union[List[int], Tuple[int, int]], value: Optional[int] = 1
    ) -> None: ...

    def overlap(
            self, othermask: Mask, offset: _Offset
    ) -> Union[Tuple[int, int], None]: ...

    def overlap_area(self, othermask: Mask, offset: _Offset) -> int: ...

    def overlap_mask(self, othermask: Mask, offset: _Offset) -> Mask: ...

    def fill(self) -> None: ...

    def clear(self) -> None: ...

    def invert(self) -> None: ...

    def scale(self, size: Union[List[int], Tuple[int, int]]) -> Mask: ...

    def draw(self, othermask: Mask, offset: _Offset) -> None: ...

    def erase(self, othermask: Mask, offset: _Offset) -> None: ...

    def count(self) -> int: ...

    def centroid(self) -> Tuple[int, int]: ...

    def angle(self) -> float: ...

    def outline(self, every: Optional[int] = 1) -> List[Tuple[int, int]]: ...

    def convolve(
            self,
            othermask: Mask,
            outputmask: Optional[Mask] = None,
            offset: Optional[_Offset] = (0, 0),
    ) -> Mask: ...

    def connected_component(
            self, pos: Union[List[int], Tuple[int, int]] = (-1, -1)
    ) -> Mask: ...

    def connected_components(self, min: Optional[int] = 0) -> List[Mask]: ...

    def get_bounding_rects(self) -> Rect: ...

    def to_surface(
            self,
            surface: Optional[Surface] = None,
            setsurface: Optional[Surface] = None,
            unsetsurface: Optional[Surface] = None,
            setcolor: Optional[_ToSurfaceColorValue] = (255, 255, 255, 255),
            unsetcolor: Optional[_ToSurfaceColorValue] = (0, 0, 0, 255),
            dest: Optional[Union[_RectValue, _Coordinate]] = (0, 0),
    ) -> Surface: ...
