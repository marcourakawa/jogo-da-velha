class Board():
    def __init__(self):
        """
        Incicializa o tabuleiro 3x3 vazio.
        """
        self.size = 3
        self.grid = [[" " for _ in range(self.size )] for _ in range(self.size)]
        self.move_count = 0

    def show(self):
        """
        Exibe o tabuleiro no terminal.
        """
        print("\n")
        for row in self.grid:
            print("|".join(row))
            print("-" * 9)

    def is_position_free(self, row, col):
        """
        Verificar se a posição está livre.
        """
        return self.grid[row][col] == " "

    def mark_position(self, row, col, symbol):
        """
        Marca uma posição com X ou O.
        """
        if self.is_position_free(row, col):
            self.grid[row][col] = symbol
            self.move_count += 1
            return True
        return False
    
    def is_full(self):
        """
        Verificar se o tabuleiro está cheio.
        """
        return self.moves_count == self.size * self.size
    