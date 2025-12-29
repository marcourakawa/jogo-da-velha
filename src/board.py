class Board:
    def __init__(self):
        self.positions = [" " for _ in range(9)]

    def show(self):
        print()
        for i in range(0, 9, 3):
            print(self.positions[i] + " | " + self.positions[i+1] + " | " + self.positions[i+2])
            if i < 6:
                print("--+---+--")
        print()

    def make_move(self, position, symbol):
        if self.positions[position] == " ":
            self.positions[position] = symbol
            return True
        return False

    def check_winner(self, symbol):
        wins = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        return any(all(self.positions[i] == symbol for i in combo) for combo in wins)

    def is_full(self):
        return " " not in self.positions
