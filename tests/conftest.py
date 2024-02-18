import pytest

from tic_tac_toe.board.board import Board
from tic_tac_toe.board.cell import CellPosition
from tic_tac_toe.board.player_id import PlayerId


@pytest.fixture
def empty_board() -> Board:
    return Board()


@pytest.fixture
def one_play_board(empty_board: Board) -> Board:
    return empty_board.play(
        player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER
    )
