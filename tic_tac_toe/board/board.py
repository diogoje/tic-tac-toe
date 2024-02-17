from __future__ import annotations

from enum import Enum

from tic_tac_toe.board.cell import CellPosition, CellStatus
from tic_tac_toe.board.mappings import (
    CELL_POSITION_BOARD_POSITION_MAPPING,
    CELL_STATUS_PLAYER_ID_MAPPING,
    PLAYER_ID_CELL_STATUS_MAPPING,
)
from tic_tac_toe.board.player_id import PlayerId

Board_Line = list[CellStatus]
Board_Data_Structure = list[list[CellStatus]]


class Board(Board_Data_Structure):
    def __init__(self) -> None:
        super().__init__([[CellStatus.EMPTY] * 3 for _ in range(3)])

    def __str__(self) -> str:
        inline_separator = " | "
        row_separator = "\n" + "-" * 9 + "\n"

        first_line = "\n"
        last_line = ""

        return (
            first_line
            + row_separator.join(inline_separator.join(row) for row in self)
            + last_line
        )

    def play(self, player_id: PlayerId, cell_position: CellPosition) -> Board:
        if not self._is_player_turn(player_id):
            raise PlayerTurnError(f"This is player {self.player_in_turn} turn.")

        if not self._is_empty_cell(cell_position):
            raise NonEmptyCellError(
                f"Player {CELL_STATUS_PLAYER_ID_MAPPING[self._get_cell_status(cell_position)]}"
                f" already played in the {cell_position} cell."
            )

        self._set_cell_status(player_id, cell_position)
        return self

    def _is_player_turn(self, player_id: PlayerId) -> bool:
        return player_id == self.player_in_turn

    @property
    def player_in_turn(self) -> PlayerId:
        return (
            PlayerId.PLAYER_1
            if self.non_empty_cells_count % 2 == 0
            else PlayerId.PLAYER_2
        )

    @property
    def non_empty_cells_count(self) -> int:
        return sum(1 for row in self for cell in row if cell != CellStatus.EMPTY)

    def _is_empty_cell(self, cell_position: CellPosition) -> bool:
        return self._get_cell_status(cell_position) == CellStatus.EMPTY

    def _get_cell_status(self, cell_position: CellPosition) -> CellStatus:
        cell_row, cell_column = CELL_POSITION_BOARD_POSITION_MAPPING[cell_position]
        return self[cell_row][cell_column]

    def _set_cell_status(
        self, player_id: PlayerId, cell_position: CellPosition
    ) -> None:
        cell_row, cell_column = CELL_POSITION_BOARD_POSITION_MAPPING[cell_position]
        cell_status = PLAYER_ID_CELL_STATUS_MAPPING[player_id]

        self[cell_row][cell_column] = cell_status

    @property
    def game_status(self) -> GameStatus:
        for line in self._get_lines_of_three():
            if self._is_three_in_a_line(line):
                return GameStatus(CELL_STATUS_PLAYER_ID_MAPPING[line[0]])

        if self._is_board_full():
            return GameStatus.DRAW

        return GameStatus.ONGOING

    def _get_lines_of_three(self) -> Board_Data_Structure:
        return self + self._get_transposed_board() + self._get_board_diagonals()

    def _get_transposed_board(self) -> Board_Data_Structure:
        return [[row[column] for row in self] for column in range(3)]

    def _get_board_diagonals(self) -> Board_Data_Structure:
        return [
            [self[0][0], self[1][1], self[2][2]],
            [self[0][2], self[1][1], self[2][0]],
        ]

    def _is_three_in_a_line(self, line: Board_Line) -> bool:
        first_cell = line[0]
        return all(
            cell == first_cell and first_cell != CellStatus.EMPTY for cell in line
        )

    def _is_board_full(self) -> bool:
        return self.non_empty_cells_count == 9


class GameStatus(Enum):
    ONGOING = "ongoing"
    DRAW = "draw"
    WINNER_PLAYER_1 = PlayerId.PLAYER_1
    WINNER_PLAYER_2 = PlayerId.PLAYER_2


class NonEmptyCellError(Exception):
    pass


class PlayerTurnError(Exception):
    pass
