from tic_tac_toe.board.board import Board
from tic_tac_toe.board.player_id import PlayerId
from tic_tac_toe.game import game
from tic_tac_toe.players.user_player import UserPlayer

if __name__ == "__main__":
    board = Board()
    player_1 = UserPlayer(PlayerId.PLAYER_1)
    player_2 = UserPlayer(PlayerId.PLAYER_2)

    result = game(board=board, player_1=player_1, player_2=player_2)

    print(board)
    print(result)
