import conf
from piece import Piece


class Pawn(Piece):
    def __init__(self, board, square, color):
        super(Pawn, self).__init__(board, square, color)
