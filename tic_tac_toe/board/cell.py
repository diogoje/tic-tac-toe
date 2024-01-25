from enum import StrEnum, auto


class CellStatus(StrEnum):
    EMPTY = " "
    PLAYER_1 = "O"
    PLAYER_2 = "X"


class CellPosition(StrEnum):
    NORTH_WEST = auto()
    NORTH = auto()
    NORTH_EAST = auto()

    WEST = auto()
    CENTER = auto()
    EAST = auto()

    SOUTH_WEST = auto()
    SOUTH = auto()
    SOUTH_EAST = auto()
