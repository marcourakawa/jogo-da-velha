# Importa a classe Game, responsável por controlar toda a lógica do jogo
from game import Game


# Esse bloco garante que o código só será executado quando este arquivo for executado diretamente, e NÃO quando ele for importado por outro arquivo.
if __name__ == "__main__":

    # Cria uma instância do jogo
    game = Game()

    # Inicia o jogo chamando o método principal
    game.play()
