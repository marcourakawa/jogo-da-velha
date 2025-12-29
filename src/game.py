from board import Board
from player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("Jogador 1", "X")
        self.player2 = Player("Jogador 2", "O")
        self.current_player = self.player1

    def switch_player(self):
        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )

    def play(self):
        print("🎮 JOGO DA VELHA")

        while True:
            self.board.show()
            move = self.current_player.make_move()

            if self.board.make_move(move, self.current_player.symbol):
                if self.board.check_winner(self.current_player.symbol):
                    self.board.show()
                    print(f"{self.current_player.name} venceu!")
                    break

                if self.board.is_full():
                    self.board.show()
                    print("Empate!")
                    break

                self.switch_player()
            else:
                print("Posição ocupada.")
