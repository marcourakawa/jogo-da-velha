class Player:
    """
    Classe que representa um jogador do jogo da velha.
    Responsável por armazenar:
    - nome do jogador
    - símbolo (X ou O)
    - ação de escolher uma jogada
    """

    def __init__(self, name, symbol):
        """
        Construtor da classe Player.

        :param name: Nome do jogador (ex: "Jogador 1")
        :param symbol: Símbolo usado no tabuleiro ("X" ou "O")
        """

        # Nome do jogador
        self.name = name

        # Símbolo que será usado no tabuleiro
        self.symbol = symbol


    def make_move(self):
        """
        Método responsável por pedir ao jogador
        a posição onde ele deseja jogar.

        Retorna:
            Um número inteiro entre 0 e 8
        """

        # Loop infinito até o jogador digitar algo válido
        while True:
            try:
                # Pede ao jogador um número de 0 a 8
                move = int(
                    input(f"{self.name} ({self.symbol}), escolha uma posição (0 a 8): ")
                )

                # Verifica se o número está dentro do intervalo permitido
                if 0 <= move <= 8:
                    return move  # Jogada válida

                # Caso o número esteja fora do intervalo
                print("Posição inválida. Escolha um número entre 0 e 8.")

            except ValueError:
                # Captura erro caso o usuário digite algo que não seja número
                print("Digite um número válido.")
