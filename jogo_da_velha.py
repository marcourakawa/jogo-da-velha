# JOGO DA VELHA



# TABULEIRO
class Board:
    def __init__(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        
    def show_board(self):
        for i in self.board():
            print("|".join(i))
        
# JOGADOR
class Player():
    pass


# JOGO
class Game():
    pass
        


a = Board()
a.show_board()