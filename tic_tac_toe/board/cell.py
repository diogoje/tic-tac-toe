from enum import Enum, StrEnum


class CellStatus(StrEnum):
    EMPTY = " "
    PLAYER_1 = "O"
    PLAYER_2 = "X"


class CellPosition(Enum):
    NORTH_WEST = (0, 0)
    NORTH = (0, 1)
    NORTH_EAST = (0, 2)

    WEST = (1, 0)
    CENTER = (1, 1)
    EAST = (1, 2)

    SOUTH_WEST = (2, 0)
    SOUTH = (2, 1)
    SOUTH_EAST = (2, 2)
