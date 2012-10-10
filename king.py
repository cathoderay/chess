from piece import Piece
from board import Board


class King(Piece):
    def __init__(self, board, square, color):
        super(King, self).__init__(board, square, color)

    def attacking_moves(self):
        return filter(lambda square: self.board.color(square) == self.opposite_color,
                      self.square.adjacents())

    def valid_moves(self):
        moves = filter(lambda square: self.board.is_empty(square),
                       self.square.adjacents())
        moves.extend(self.attacking_moves())
        return moves
