from piece import Piece
from board import Board


class King(Piece):
    def __init__(self, board, square, color):
        super(King, self).__init__(board, square, color)

    def adjacent_squares(self):
        return filter(lambda x: x is not None,
                       [self.square.northwest(),
                        self.square.north(),
                        self.square.northeast(),
                        self.square.west(),
                        self.square.east(),
                        self.square.southwest(),
                        self.square.south(),
                        self.square.southeast()])

    def attacking_moves(self):
        return filter(lambda x: self.board.color(x) == self.opposite_color(),
                      self.adjacent_squares())

    def valid_moves(self):
        moves = filter(lambda x: self.board.is_empty(x),
                       self.adjacent_squares())
        moves.extend(self.attacking_moves())
        return moves
