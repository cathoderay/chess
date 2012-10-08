from itertools import takewhile

from piece import Piece


class Rook(Piece):
    def __init__(self, board, square, color):
        super(Rook, self).__init__(board, square, color)

    def till_piece(self, func):
       return [s for s in takewhile(lambda x: self.board.is_empty(x), func())]

    def valid_moves(self):
        norths = self.till_piece(self.square.norths)
        souths = self.till_piece(self.square.souths)
        wests = self.till_piece(self.square.wests)
        easts = self.till_piece(self.square.easts)
        moves = norths + souths + wests + easts
        return moves
