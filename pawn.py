import conf
from piece import Piece
from square import Square


class Pawn(Piece):
    def __init__(self, board, square, color):
        super(Pawn, self).__init__(board, square, color)

    def ahead(self, square, color):
        if color == conf.WHITE:
            return square.north()
        return square.south()

    def northeast(self):
        if self.color == conf.WHITE:
            return self.square.northeast()
        return self.square.southeast()

    def northwest(self):
        if self.color == conf.WHITE:
            return self.square.northwest()
        return self.square.southwest()

    def can_move_one_square(self):
       ahead = self.ahead(self.square, self.color)
       return (self.board.is_empty(ahead), ahead)

    def can_move_two_squares(self, pos):
        ahead = self.ahead(pos, self.color)
        return (ahead and self.board.is_empty(ahead), ahead)

    def attacking_moves(self):
        attacks = [self.northwest(), self.northeast()]
        attacks = filter(lambda a: a is not None and \
                                   not self.board.is_empty(a) and \
                                   self.board.color(a) == self.opposite_color(),
                         attacks)
        return attacks

    def valid_moves(self):
        moves = []
        can_move_one_square, ahead = self.can_move_one_square()
        if can_move_one_square:
            moves.append(ahead)
            can_move_two_squares, ahead = self.can_move_two_squares(ahead)
            if can_move_two_squares:
                moves.append(ahead)
        moves.extend(self.attacking_moves())
        return moves
