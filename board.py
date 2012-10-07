import string

from conf import EMPTY, INITIAL_BOARD, WHITE, BLACK
from square import Square
from exception import InvalidBoard


class Board:
    valid = set('rRnNbBqQkKpP.')

    def __init__(self):
        self.reset()

    def set_config(self, matrix=None, flat=None):
        Board.validate(matrix=matrix, flat=flat)
        self.matrix = matrix or Board.to_matrix(flat)

    def reset(self):
        self.matrix = Board.to_matrix(INITIAL_BOARD)

    def move(self, a, b):
        piece = self.matrix[a[0]][a[1]]
        self.matrix[a[0]][a[1]] = EMPTY
        self.matrix[b[0]][b[1]] = piece

    def clean(self):
        self.set_config(flat=EMPTY*64)

    def is_empty(self, tup):
        if isinstance(tup, Square):
            tup = tup.tuple
        return self.matrix[tup[0]][tup[1]] == EMPTY

    def is_black(self, tup):
        return self.matrix[tup[0]][tup[1]].isupper()

    def is_white(self, tup):
        return self.matrix[tup[0]][tup[1]].islower()

    def color(self, tup):
        if isinstance(tup, Square):
            tup = tup.tuple
        if self.is_black(tup):
            return BLACK
        elif self.is_white(tup):
            return WHITE
        return None

    @classmethod
    def to_flat(self, matrix):
        return ''.join([e for l in matrix
                          for e in l])

    @classmethod
    def to_matrix(self, flat):
        return [list(flat[l*8:l*8+8])
                for l in xrange(8)]

    @classmethod
    def validate(self, matrix=None, flat=None):
        flat = flat or Board.to_flat(matrix)
        if len(flat) != 64 or not \
           set(flat).issubset(self.valid):
            raise InvalidBoard

    def __repr__(self):
        header = footer = "\n%s%s%s\n" %("  .-", " -"*6, " -.")
        board = '\n'.join(["%s |%s|" % (8 - i, ' '.join(l))
                           for i, l in enumerate(self.matrix)])
        alpha = "   %s\n" % " ".join(string.lowercase[:8])
        return header + board + footer + alpha

