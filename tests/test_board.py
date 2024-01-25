from typing import Optional
import pytest


from tic_tac_toe.board.board import Board, NotEmptyCellError, PlayerTurnError
from tic_tac_toe.board.cell import CellStatus, CellPosition
from tic_tac_toe.board.player_id import PlayerId


@pytest.fixture
def empty_board() -> Board:
    return Board()


@pytest.fixture
def one_play_board() -> Board:
    return Board().play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)


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
    with pytest.raises(NotEmptyCellError):
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.CENTER)
        )
    with pytest.raises(NotEmptyCellError):
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.CENTER)
        )
    with pytest.raises(NotEmptyCellError):
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.NORTH_EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_WEST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_WEST)
        )


@pytest.mark.parametrize(
    ("board", "winner"),
    (
        (Board(), None),
        (
            Board().play(
                player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER
            ),
            None,
        ),
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH),
            None,
        ),
        # Center vertical
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.NORTH)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_WEST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.SOUTH),
            PlayerId.PLAYER_1,
        ),
        # Center horizontal
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.SOUTH_EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.WEST),
            PlayerId.PLAYER_1,
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
            PlayerId.PLAYER_2,
        ),
        # Positive diagonal
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.SOUTH_WEST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.WEST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.NORTH_EAST),
            PlayerId.PLAYER_1,
        ),
        # Negative diagonal
        (
            Board()
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.CENTER)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.NORTH_EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.SOUTH_EAST)
            .play(player_id=PlayerId.PLAYER_2, cell_position=CellPosition.EAST)
            .play(player_id=PlayerId.PLAYER_1, cell_position=CellPosition.NORTH_WEST),
            PlayerId.PLAYER_1,
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
            PlayerId.PLAYER_2,
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
            None,
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
            PlayerId.PLAYER_1,
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
            PlayerId.PLAYER_2,
        ),
    ),
)
def test_end_game(board: Board, winner: Optional[PlayerId]) -> None:
    assert board.get_winner() == winner


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
