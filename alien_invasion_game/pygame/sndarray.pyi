from typing import Tuple
from pygame.mixer import Sound
import numpy


def array(sound: Sound) -> numpy.ndarray: ...


def samples(sound: Sound) -> numpy.ndarray: ...


def make_sound(array: numpy.ndarray) -> Sound: ...


def use_arraytype(arraytype: str) -> Sound: ...


def get_arraytype() -> str: ...


def get_arraytypes() -> Tuple[str]: ...
