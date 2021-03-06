from itertools import takewhile

from piece import Piece


class Rook(Piece):
    def __init__(self, board, square, color):
        super(Rook, self).__init__(board, square, color)

    def till_piece(self, sense_func):
       return [s for s in takewhile(lambda x: self.board.is_empty(x),
                                    sense_func())]

    def attacking_move(self, sense_func):
        try:
            candidate = filter(lambda x: not self.board.is_empty(x), 
                               sense_func())[0]
        except IndexError:
            return None
        return candidate \
               if self.board.color(candidate) == self.opposite_color \
               else None

    def attacking_moves(self):
        return filter(lambda x: x,
                      [self.attacking_move(self.square.norths),
                       self.attacking_move(self.square.souths),
                       self.attacking_move(self.square.wests),
                       self.attacking_move(self.square.easts)])

    def valid_moves(self):
        norths = self.till_piece(self.square.norths)
        souths = self.till_piece(self.square.souths)
        wests = self.till_piece(self.square.wests)
        easts = self.till_piece(self.square.easts)
        moves = norths + souths + wests + easts
        moves.extend(self.attacking_moves())
        return moves
