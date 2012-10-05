from board import Board
from exception import OutOfBoard


class Piece(object):
    def __init__(self, board=Board(), square=None, color=None):
        self.has_moved = False
        self.board = board
        self.square = square
        self.color = color

    def is_legal(self, move):
        raise NotImplementedError()

    def valid_moves(self):
        raise NotImplementedError()
