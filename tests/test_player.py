from unittest.mock import patch

import pytest

from tic_tac_toe.board.board import Board
from tic_tac_toe.board.cell import CellPosition
from tic_tac_toe.board.player_id import PlayerId
from tic_tac_toe.players.players import UserPlayer


@pytest.fixture
def user_player() -> UserPlayer:
    return UserPlayer(PlayerId.PLAYER_1)


@pytest.fixture
def board() -> Board:
    return Board().play(
        player_id=PlayerId.PLAYER_1,
        cell_position=CellPosition.CENTER,
    )


@pytest.mark.parametrize(
    ("cell_position_input", "expected_cell_position"),
    (
        ("north_west", CellPosition.NORTH_WEST),
        ("north", CellPosition.NORTH),
        ("north_east", CellPosition.NORTH_EAST),
        ("west", CellPosition.WEST),
        ("center", CellPosition.CENTER),
        ("east", CellPosition.EAST),
        ("south_west", CellPosition.SOUTH_WEST),
        ("south", CellPosition.SOUTH),
        ("south_east", CellPosition.SOUTH_EAST),
    ),
)
def test_user_player_valid_play(
    user_player: UserPlayer,
    board: Board,
    cell_position_input: str,
    expected_cell_position: CellPosition,
) -> None:
    with patch("builtins.input", return_value=cell_position_input):
        assert user_player.get_play(board) == expected_cell_position


@pytest.mark.parametrize(
    "cell_position_consecutive_inputs",
    (["", " ", "up", "north"], ["down", "south"], ["right", "east"]),
)
def test_user_player_invalid_play(
    user_player: UserPlayer, board: Board, cell_position_consecutive_inputs: list[str]
) -> None:
    with patch("builtins.input", side_effect=cell_position_consecutive_inputs):
        user_player.get_play(board)
