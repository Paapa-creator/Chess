import string


class Piece:
    def __init__(self,  symbol=None, vector=None,):
        self.vector = vector
        self.symbol = symbol


class Knight(Piece):
    def __init__(self, pos, colour):
        super().__init__(symbol="N", vector=[1, 2])
        self.pos = pos
        self.colour = colour


class Bishop(Piece):
    def __init__(self, pos, colour):
        super().__init__(symbol="B", vector=[1, 1])
        self.pos = pos
        self.colour = colour


class Queen(Piece):
    def __init__(self, pos, colour):
        super().__init__(symbol='Q', vector=[])
        self.pos = pos
        self.colour = colour


class King(Piece):
    def __init__(self, pos, colour):
        super().__init__(symbol='K', vector=[1])
        self.pos = pos
        self.colour = colour


class Rook(Piece):
    def __init__(self, pos, colour):
        super().__init__(symbol='R', vector=[1, 0])
        self.pos = pos
        self.colour = colour


class Pawn(Piece):
    def __init__(self, pos, colour):
        super().__init__(symbol='', vector=[0, 1])
        self.pos = pos
        self.colour = colour


class Board:
    def __init__(self):
        self.pieces = []
        # white pieces

        # knights
        self.white_knight_light = Knight('b1', 'w')
        self.pieces.append(self.white_knight_light)

        self.white_knight_dark = Knight('g1', 'w')
        self.pieces.append(self.white_knight_dark)

        # Bishops
        self.white_bishop_light = Bishop('f1', 'w')
        self.pieces.append(self.white_bishop_light)

        self.white_bishop_dark = Bishop('c1', 'w')
        self.pieces.append(self.white_bishop_dark)

        # Rooks
        self.white_rook_light = Rook('h1', 'w')
        self.pieces.append(self.white_rook_light)

        self.white_rook_dark = Rook('a1', 'w')
        self.pieces.append(self.white_rook_dark)

        # Queen
        self.white_queen = Queen('d1', 'w')
        self.pieces.append(self.white_queen)

        # King
        self.white_king = King('e1', 'w')
        self.pieces.append(self.white_king)

        # pawns
        self.white_pawn1 = Pawn('a2', 'w')
        self.pieces.append(self.white_pawn1)

        self.white_pawn2 = Pawn('b2', 'w')
        self.pieces.append(self.white_pawn2)

        self.white_pawn3 = Pawn('c2', 'w')
        self.pieces.append(self.white_pawn3)

        self.white_pawn4 = Pawn('d2', 'w')
        self.pieces.append(self.white_pawn4)

        self.white_pawn5 = Pawn('e2', 'w')
        self.pieces.append(self.white_pawn5)

        self.white_pawn6 = Pawn('f2', 'w')
        self.pieces.append(self.white_pawn6)

        self.white_pawn7 = Pawn('g2', 'w')
        self.pieces.append(self.white_pawn7)

        self.white_pawn8 = Pawn('h2', 'w')
        self.pieces.append(self.white_pawn8)

        # black pieces

        # knights
        self.black_knight_light = Knight('g8', 'b')
        self.pieces.append(self.black_knight_light)

        self.black_knight_dark = Knight('b8', 'b')
        self.pieces.append(self.black_knight_dark)

        # bishops
        self.black_bishop_light = Bishop('c8', 'b')
        self.pieces.append(self.black_bishop_light)

        self.black_bishop_dark = Bishop('f8', 'b')
        self.pieces.append(self.black_bishop_dark)

        # Rooks
        self.black_rook_light = Rook('h8', 'b')
        self.pieces.append(self.black_rook_light)

        self.black_rook_dark = Rook('a8', 'b')
        self.pieces.append(self.black_rook_dark)

        # Queen
        self.black_queen = Queen('d8', 'b')
        self.pieces.append(self.black_queen)

        # King
        self.black_king = King('e8', 'b')
        self.pieces.append(self.black_king)

        # pawns
        self.black_pawn1 = Pawn('a7', 'b')
        self.pieces.append(self.black_pawn1)

        self.black_pawn2 = Pawn('b7', 'b')
        self.pieces.append(self.black_pawn2)

        self.black_pawn3 = Pawn('c7', 'b')
        self.pieces.append(self.black_pawn3)

        self.black_pawn4 = Pawn('d7', 'b')
        self.pieces.append(self.black_pawn4)

        self.black_pawn5 = Pawn('e7', 'b')
        self.pieces.append(self.black_pawn5)

        self.black_pawn6 = Pawn('f7', 'b')
        self.pieces.append(self.black_pawn6)

        self.black_pawn7 = Pawn('g7', 'b')
        self.pieces.append(self.black_pawn7)

        self.black_pawn8 = Pawn('h7', 'b')
        self.pieces.append(self.black_pawn8)

        self.files = [file for file in list(string.ascii_lowercase)[:8]]
        self.ranks = [rank for rank in range(1, 9)]
        self.squares = [str(file) + str(rank) for rank in self.ranks for file in self.files]

        self.board = {

        }
        for square in self.squares:
            self.board.update({square: None})

        for piece in self.pieces:
            self.board[piece.pos] = piece


test = Board()
print(test.board)