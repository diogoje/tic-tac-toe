from unittest.mock import MagicMock, PropertyMock, patch

import pytest

import tic_tac_toe.game
from tic_tac_toe.board.board import Board, GameStatus
from tic_tac_toe.board.player_id import PlayerId
from tic_tac_toe.game import Player, PlayerIdError, Result, _verify_player_ids, game


@pytest.fixture
def player_1() -> MagicMock:
    return MagicMock(spec=Player, player_id=PlayerId.PLAYER_1)


@pytest.fixture
def player_2() -> MagicMock:
    return MagicMock(spec=Player, player_id=PlayerId.PLAYER_2)


@pytest.fixture
def board() -> MagicMock:
    return MagicMock(spec=Board)


@pytest.mark.parametrize(
    ("player_1_fixture", "player_2_fixture"),
    (
        ("player_1", "player_1"),
        ("player_2", "player_1"),
        ("player_2", "player_2"),
    ),
)
def test_verify_player_ids(
    player_1_fixture: str, player_2_fixture: str, request: pytest.FixtureRequest
) -> None:
    with pytest.raises(PlayerIdError):
        _verify_player_ids(
            player_1=request.getfixturevalue(player_1_fixture),
            player_2=request.getfixturevalue(player_2_fixture),
        )


@pytest.mark.parametrize(
    "expected_result",
    (GameStatus.DRAW, GameStatus.WINNER_PLAYER_1, GameStatus.WINNER_PLAYER_2),
)
@patch.object(tic_tac_toe.game, "_verify_player_ids")
def test_game(
    mock_verify_player_ids: MagicMock,
    board: MagicMock,
    player_1: MagicMock,
    player_2: MagicMock,
    expected_result: Result,
) -> None:
    type(board).player_in_turn = PropertyMock(
        side_effect=(PlayerId.PLAYER_1, PlayerId.PLAYER_2)
    )
    type(board).game_status = PropertyMock(
        side_effect=(
            GameStatus.ONGOING,
            GameStatus.ONGOING,
            expected_result,
            expected_result,
        )
    )

    result = game(board=board, player_1=player_1, player_2=player_2)

    mock_verify_player_ids.assert_called_once_with(player_1, player_2)
    player_1.play.assert_called_once_with(board)
    player_2.play.assert_called_once_with(board)
    assert result == expected_result
