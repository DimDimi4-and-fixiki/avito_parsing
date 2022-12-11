from __future__ import annotations

from enum import Enum


class City(str, Enum):
    MOSCOW = 'moskva'
    SPB = 'sankt_peterburg_i_lo'
    SOCHI = 'sochi'
