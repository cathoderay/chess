from conf import BLACK, WHITE
from board import Board


class Piece(object):
    def __init__(self, board=Board(), square=None, color=None):
        self.has_moved = False
        self.board = board
        self.square = square
        self.color = color

    @property
    def opposite_color(self):
        return BLACK if self.color == WHITE else WHITE

    def is_valid(self, move):
        return move in self.valid_moves()

    def valid_moves(self):
        raise NotImplementedError()
