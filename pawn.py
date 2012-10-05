import conf
from piece import Piece
from square import Square


class Pawn(Piece):
    def __init__(self, board, square, color):
        super(Pawn, self).__init__(board, square, color)

    def move_forward(self):
        last_square = self.square
        if self.color == conf.WHITE:
            self.square = self.square.north()
        else:
            self.square = self.square.south()
        self.board.notify_move(last_square, self.square)

