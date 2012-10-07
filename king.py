from piece import Piece
from board import Board


class King(Piece):
    def __init__(self, board, square, color):
        super(King, self).__init__(board, square, color)

    def valid_moves(self):
        moves = [self.square.northwest(),
                 self.square.north(),
                 self.square.northeast(),
                 self.square.west(),
                 self.square.east(),
                 self.square.southwest(),
                 self.square.south(),
                 self.square.southeast()]
        moves = filter(lambda x: x and
                                 self.board.is_empty(x),
                       moves)
        return moves
