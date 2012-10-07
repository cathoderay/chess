from piece import Piece
from board import Board


class King(Piece):
    def __init__(self, board, square, color):
        super(King, self).__init__(board, square, color)

