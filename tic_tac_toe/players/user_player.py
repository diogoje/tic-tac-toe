from dataclasses import dataclass

from tic_tac_toe.board.board import Board, NonEmptyCellError
from tic_tac_toe.board.cell import CellPosition
from tic_tac_toe.board.mappings import PLAYER_ID_CELL_STATUS_MAPPING
from tic_tac_toe.board.player_id import PlayerId


@dataclass
class UserPlayer:
    player_id: PlayerId

    def play(self, board: Board) -> Board:
        print(board, end="\n" * 2)

        cell_position_input = self._request_first_input()

        while True:
            try:
                cell_position = CellPosition(cell_position_input)
                board.play(player_id=self.player_id, cell_position=cell_position)
            except (ValueError, NonEmptyCellError):
                cell_position_input = self._request_input_after_invalid_input()
            else:
                break

        return board

    def _request_first_input(self) -> str:
        return input(
            f"Player {self.player_id} turn:"
            f" {PLAYER_ID_CELL_STATUS_MAPPING[self.player_id]}\n"
            "Where do you want to play next? "
        )

    def _request_input_after_invalid_input(self) -> str:
        return input("Invalid cell position. Try again: ")
