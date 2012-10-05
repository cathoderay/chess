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

    def can_move_one_square(self):
       ahead = self.ahead(self.square, self.color)
       return (self.board.is_empty(ahead), ahead)

    def can_move_two_squares(self, pos):
        ahead = self.ahead(pos, self.color)
        return (ahead and self.board.is_empty(ahead), 
                ahead)

    def valid_moves(self):
        moves = []
        can_move_one_square, ahead = self.can_move_one_square()
        if can_move_one_square:
            moves.append(ahead)
            can_move_two_squares, ahead = self.can_move_two_squares(ahead)
            if can_move_two_squares:
                moves.append(ahead)
        return moves 
