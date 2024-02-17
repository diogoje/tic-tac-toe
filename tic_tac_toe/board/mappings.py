from tic_tac_toe.board.cell import CellStatus
from tic_tac_toe.board.player_id import PlayerId


PLAYER_ID_CELL_STATUS_MAPPING = {
    PlayerId.PLAYER_1: CellStatus.PLAYER_1,
    PlayerId.PLAYER_2: CellStatus.PLAYER_2,
}

CELL_STATUS_PLAYER_ID_MAPPING = {
    value: key for key, value in PLAYER_ID_CELL_STATUS_MAPPING.items()
}
