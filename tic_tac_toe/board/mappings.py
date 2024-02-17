from tic_tac_toe.board.cell import CellStatus, CellPosition
from tic_tac_toe.board.player_id import PlayerId


PLAYER_ID_CELL_STATUS_MAPPING = {
    PlayerId.PLAYER_1: CellStatus.PLAYER_1,
    PlayerId.PLAYER_2: CellStatus.PLAYER_2,
}

CELL_STATUS_PLAYER_ID_MAPPING = {
    value: key for key, value in PLAYER_ID_CELL_STATUS_MAPPING.items()
}


CELL_POSITION_BOARD_POSITION_MAPPING: dict[CellPosition, tuple[int, int]] = {
    CellPosition.NORTH_WEST: (0, 0),
    CellPosition.NORTH: (0, 1),
    CellPosition.NORTH_EAST: (0, 2),
    CellPosition.WEST: (1, 0),
    CellPosition.CENTER: (1, 1),
    CellPosition.EAST: (1, 2),
    CellPosition.SOUTH_WEST: (2, 0),
    CellPosition.SOUTH: (2, 1),
    CellPosition.SOUTH_EAST: (2, 2),
}
