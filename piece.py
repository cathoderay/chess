import conf
from board import Board


class Piece(object):
    def __init__(self, board=Board(), square=None, color=None):
        self.has_moved = False
        self.board = board
        self.square = square
        self.color = color

    def opposite_color(self):
        return conf.BLACK if self.color == conf.WHITE else conf.WHITE

    def is_legal(self, move):
        raise NotImplementedError()

    def valid_moves(self):
        raise NotImplementedError()
