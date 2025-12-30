class Board:
    """
    Classe responsável por representar o tabuleiro do jogo da velha.

    Responsabilidades:
    - Armazenar o estado do tabuleiro
    - Exibir o tabuleiro
    - Validar jogadas
    - Verificar vitória
    - Verificar empate
    """

    def __init__(self):
        """
        Construtor da classe Board.

        É executado automaticamente quando o objeto é criado.
        Inicializa o tabuleiro com 9 posições vazias.
        """

        # Lista com 9 espaços vazios
        # Cada índice representa uma posição do tabuleiro:
        #
        #  0 | 1 | 2
        #  3 | 4 | 5
        #  6 | 7 | 8
        #
        self.positions = [" " for _ in range(9)]


    def show(self):
        """
        Exibe o tabuleiro no terminal de forma visual.
        """

        print()  # Espaço visual antes do tabuleiro

        # Percorre o tabuleiro de 3 em 3 posições
        for i in range(0, 9, 3):

            # Exibe uma linha do tabuleiro
            print(
                self.positions[i] + " | " +
                self.positions[i + 1] + " | " +
                self.positions[i + 2]
            )

            # Imprime separador entre as linhas
            if i < 6:
                print("--+---+--")

        print()  # Espaço visual depois do tabuleiro


    def make_move(self, position, symbol):
        """
        Realiza uma jogada no tabuleiro.

        :param position: posição escolhida (0 a 8)
        :param symbol: símbolo do jogador ('X' ou 'O')
        :return: True se a jogada for válida, False caso contrário
        """

        # Verifica se a posição está vazia
        if self.positions[position] == " ":
            self.positions[position] = symbol
            return True  # Jogada realizada com sucesso

        # Caso a posição já esteja ocupada
        return False


    def check_winner(self, symbol):
        """
        Verifica se o jogador atual venceu.

        :param symbol: símbolo do jogador ('X' ou 'O')
        :return: True se venceu, False caso contrário
        """

        # Todas as combinações possíveis de vitória
        wins = [
            [0, 1, 2],  # linha superior
            [3, 4, 5],  # linha do meio
            [6, 7, 8],  # linha inferior

            [0, 3, 6],  # coluna esquerda
            [1, 4, 7],  # coluna do meio
            [2, 5, 8],  # coluna direita

            [0, 4, 8],  # diagonal principal
            [2, 4, 6]   # diagonal secundária
        ]

        # Retorna True se qualquer combinação for vencedora
        return any(
            all(self.positions[i] == symbol for i in combo)
            for combo in wins
        )


    def is_full(self):
        """
        Verifica se o tabuleiro está cheio.

        :return: True se não houver mais espaços vazios
        """

        return " " not in self.positions
