import string


class Chess:
    def __init__(self):
        self.files = [file for file in list(string.ascii_lowercase)[:8]]
        self.ranks = [rank for rank in range(1, 9)]
        self. board = {

        }


class Piece(Chess):
    def __init__(self, vector, symbol, pos):
        super().__init__()
        self.vector = vector
        self.symbol = symbol
        self.pos = pos


knight = Piece(1, )
m = Piece(3, 3, 3)
print(m.ranks)
