from piece import Piece
from board import Board


class King(Piece):
    def __init__(self, board, square, color):
        super(King, self).__init__(board, square, color)

    def attacking_moves(self):
        return filter(lambda x: self.board.color(x) == self.opposite_color(),
                      self.square.adjacents())

    def valid_moves(self):
        moves = filter(lambda x: self.board.is_empty(x),
                       self.square.adjacents())
        moves.extend(self.attacking_moves())
        return moves
