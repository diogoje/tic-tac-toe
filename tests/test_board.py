import pytest

from tic_tac_toe.board.board import (
    Board,
    GameStatus,
    NonEmptyCellError,
    PlayerTurnError,
)
from tic_tac_toe.board.cell import CellPosition, CellStatus
from tic_tac_toe.board.player_id import PlayerId


@pytest.fixture
def two_play_board() -> Board:
    return (
        Board()
        .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
        .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_WEST)
    )


@pytest.fixture
def full_board() -> Board:
    return (
        Board()
        .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
        .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_WEST)
        .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.NORTH_EAST)
        .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.SOUTH_WEST)
        .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.WEST)
        .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.EAST)
        .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.SOUTH)
        .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH)
        .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.SOUTH_EAST)
    )


@pytest.mark.parametrize(
    ("board_fixture", "board_print"),
    (
        (
            "empty_board",
            f"\n{CellStatus.EMPTY} | {CellStatus.EMPTY} | {CellStatus.EMPTY}"
            f"\n---------"
            f"\n{CellStatus.EMPTY} | {CellStatus.EMPTY} | {CellStatus.EMPTY}"
            f"\n---------"
            f"\n{CellStatus.EMPTY} | {CellStatus.EMPTY} | {CellStatus.EMPTY}",
        ),
        (
            "one_play_board",
            f"\n{CellStatus.EMPTY} | {CellStatus.EMPTY} | {CellStatus.EMPTY}"
            f"\n---------"
            f"\n{CellStatus.EMPTY} | {CellStatus.PLAYER_1} | {CellStatus.EMPTY}"
            f"\n---------"
            f"\n{CellStatus.EMPTY} | {CellStatus.EMPTY} | {CellStatus.EMPTY}",
        ),
        (
            "two_play_board",
            f"\n{CellStatus.PLAYER_2} | {CellStatus.EMPTY} | {CellStatus.EMPTY}"
            f"\n---------"
            f"\n{CellStatus.EMPTY} | {CellStatus.PLAYER_1} | {CellStatus.EMPTY}"
            f"\n---------"
            f"\n{CellStatus.EMPTY} | {CellStatus.EMPTY} | {CellStatus.EMPTY}",
        ),
        (
            "full_board",
            f"\n{CellStatus.PLAYER_2} | {CellStatus.PLAYER_2} | {CellStatus.PLAYER_1}"
            f"\n---------"
            f"\n{CellStatus.PLAYER_1} | {CellStatus.PLAYER_1} | {CellStatus.PLAYER_2}"
            f"\n---------"
            f"\n{CellStatus.PLAYER_2} | {CellStatus.PLAYER_1} | {CellStatus.PLAYER_1}",
        ),
    ),
)
def test_board_print(
    board_fixture: str, board_print: str, request: pytest.FixtureRequest
) -> None:
    assert str(request.getfixturevalue(board_fixture)) == board_print


def test_raises_cell_not_empty() -> None:
    with pytest.raises(NonEmptyCellError):
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.CENTER)
        )
    with pytest.raises(NonEmptyCellError):
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.CENTER)
        )
    with pytest.raises(NonEmptyCellError):
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.NORTH_EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_WEST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_WEST)
        )


@pytest.mark.parametrize(
    ("board", "game_status"),
    (
        (
            Board(),
            GameStatus.ONGOING,
        ),
        (
            Board().play(
                player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER
            ),
            GameStatus.ONGOING,
        ),
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH),
            GameStatus.ONGOING,
        ),
        # Center vertical
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.NORTH)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_WEST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.SOUTH),
            GameStatus.WINNER_PLAYER_1,
        ),
        # Center horizontal
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.SOUTH_EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.WEST),
            GameStatus.WINNER_PLAYER_1,
        ),
        # North
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.SOUTH_EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_WEST),
            GameStatus.WINNER_PLAYER_2,
        ),
        # Positive diagonal
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.SOUTH_WEST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.WEST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.NORTH_EAST),
            GameStatus.WINNER_PLAYER_1,
        ),
        # Negative diagonal
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.SOUTH_EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.NORTH_WEST),
            GameStatus.WINNER_PLAYER_1,
        ),
        # South
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.SOUTH)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.SOUTH_EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.NORTH_WEST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.SOUTH_WEST),
            GameStatus.WINNER_PLAYER_2,
        ),
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_WEST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.NORTH_EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.SOUTH_WEST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.WEST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.SOUTH)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.SOUTH_EAST),
            GameStatus.DRAW,
        ),
        # East
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_WEST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.WEST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.SOUTH_WEST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.NORTH_EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.SOUTH)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.SOUTH_EAST),
            GameStatus.WINNER_PLAYER_1,
        ),
        # West
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_WEST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.NORTH_EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.SOUTH_WEST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.SOUTH_EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.SOUTH)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.WEST),
            GameStatus.WINNER_PLAYER_2,
        ),
    ),
)
def test_game_status(board: Board, game_status: GameStatus) -> None:
    assert board.game_status == game_status


def test_playing_order() -> None:
    with pytest.raises(PlayerTurnError):
        Board().play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.CENTER)

    with pytest.raises(PlayerTurnError):
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.EAST)
        )

    with pytest.raises(PlayerTurnError):
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.SOUTH)
        )

    with pytest.raises(PlayerTurnError):
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
        )
