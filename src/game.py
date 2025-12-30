# Importa a classe Board, responsável pelo tabuleiro do jogo
from board import Board

# Importa a classe Player, responsável pelos jogadores
from player import Player


class Game:
    """
    Classe responsável por controlar o jogo.
    Ela conecta o tabuleiro (Board) com os jogadores (Player)
    e gerencia o fluxo da partida.
    """

    def __init__(self):
        """
        Construtor da classe Game.
        Executado automaticamente quando o jogo começa.
        """

        # Cria o tabuleiro do jogo
        self.board = Board()

        # Cria os dois jogadores
        # Cada jogador recebe um nome e um símbolo
        self.player1 = Player("Jogador 1", "X")
        self.player2 = Player("Jogador 2", "O")

        # Define quem começa o jogo
        self.current_player = self.player1


    def switch_player(self):
        """
        Alterna o jogador atual.
        Se for o jogador 1, muda para o jogador 2.
        Se for o jogador 2, muda para o jogador 1.
        """

        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )


    def play(self):
        """
        Método principal do jogo.
        Controla o loop do jogo, jogadas, vitórias e empate.
        """

        print("JOGO DA VELHA")

        # Loop infinito — só para quando alguém ganhar ou empatar
        while True:

            # Mostra o tabuleiro atual
            self.board.show()

            # Pede ao jogador atual uma posição para jogar
            move = self.current_player.make_move()

            # Tenta aplicar a jogada no tabuleiro
            if self.board.make_move(move, self.current_player.symbol):

                # Verifica se o jogador venceu
                if self.board.check_winner(self.current_player.symbol):
                    self.board.show()
                    print(f"{self.current_player.name} venceu!")
                    break  # Encerra o jogo

                # Verifica se o tabuleiro está cheio (empate)
                if self.board.is_full():
                    self.board.show()
                    print("Empate!")
                    break  # Encerra o jogo

                # Se ninguém venceu, troca o jogador
                self.switch_player()

            else:
                # Caso a posição já esteja ocupada
                print("Posição ocupada. Tente novamente.")
