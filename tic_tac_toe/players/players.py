from dataclasses import dataclass

from tic_tac_toe.board.board import Board
from tic_tac_toe.board.cell import CellPosition
from tic_tac_toe.board.mappings import PLAYER_ID_CELL_STATUS_MAPPING
from tic_tac_toe.board.player_id import PlayerId


@dataclass
class UserPlayer:
    player_id: PlayerId

    def get_play(self, board: Board) -> CellPosition:
        print(board, end="\n" * 2)

        cell_position_input = input(
            f"Player {self.player_id} turn:"
            f" {PLAYER_ID_CELL_STATUS_MAPPING[self.player_id]}\n"
            "Where do you want to play next? "
        )

        while True:
            try:
                cell_position = CellPosition(cell_position_input)
            except ValueError:
                cell_position_input = input("Invalid cell position. Try again: ")
            else:
                break

        return cell_position
