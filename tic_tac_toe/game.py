from typing import Literal, Protocol, Self

from tic_tac_toe.board.board import Board, GameStatus
from tic_tac_toe.board.player_id import PlayerId

Result = Literal[
    GameStatus.DRAW,
    GameStatus.WINNER_PLAYER_1,
    GameStatus.WINNER_PLAYER_2,
]


class Player(Protocol):
    @property
    def player_id(self: Self) -> PlayerId:
        ...

    def play(self: Self, board: Board) -> Board:
        ...


def game(board: Board, player_1: Player, player_2: Player) -> Result:
    _verify_player_ids(player_1, player_2)
    players = {player_1.player_id: player_1, player_2.player_id: player_2}

    while board.game_status == GameStatus.ONGOING:
        player_in_turn = players[board.player_in_turn]
        player_in_turn.play(board)

    return board.game_status


def _verify_player_ids(player_1: Player, player_2: Player) -> None:
    if (
        player_1.player_id != PlayerId.PLAYER_1
        or player_2.player_id != PlayerId.PLAYER_2
    ):
        raise PlayerIdError(
            first_player_id=player_1.player_id,
            second_player_id=player_2.player_id,
        )


class PlayerIdError(Exception):
    def __init__(
        self: Self,
        first_player_id: PlayerId,
        second_player_id: PlayerId,
    ) -> None:
        super().__init__(
            f"Player IDs provided: {first_player_id} and {second_player_id}."
            f" Expected: {PlayerId.PLAYER_1} and {PlayerId.PLAYER_2}.",
        )
