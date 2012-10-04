from board import Board


class Piece(object):
    def __init__(self, board=Board(), position=None, color=None):
        self.have_moved = False
        self.board = board
        self.position = position
        self.color = color

    def is_legal(self, move):
        raise NotImplementedError()

    def legal_moves(self):
        raise NotImplementedError()
