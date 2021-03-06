from typing import List, Optional, Union, Tuple
from pygame.surface import Surface


def init() -> None: ...


def quit() -> None: ...


def list_cameras() -> List[str]: ...


class Camera:
    def __init__(
            self,
            device: str,
            size: Optional[Union[Tuple[int, int], List[int]]] = (320, 200),
            format: Optional[str] = "RGB",
    ): ...

    def start(self) -> None: ...

    def stop(self) -> None: ...

    def get_controls(self) -> Tuple[bool, bool, int]: ...

    def set_controls(
            self,
            hflip: Optional[bool] = ...,
            vflip: Optional[bool] = ...,
            brightness: Optional[int] = ...,
    ) -> Tuple[bool, bool, int]: ...

    def get_size(self) -> Tuple[int, int]: ...

    def query_image(self) -> bool: ...

    def get_image(self, surface: Optional[Surface] = None) -> Surface: ...

    def get_raw(self) -> str: ...
