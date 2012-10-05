import conf
from piece import Piece
from square import Square


class Pawn(Piece):
    def __init__(self, board, square, color):
        super(Pawn, self).__init__(board, square, color)

    def move_forward(self):
        last = self.square
        if self.color == conf.WHITE:
            new = self.square.north()
        else:
            new = self.square.south()
        self.square = new
        self.board.notify_move(last.tuple, new.tuple)

