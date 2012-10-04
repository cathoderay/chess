import conf
from exception import InvalidBoard


class Board:
    valid = set('rRnNbBqQkKpP_')

    def __init__(self):
        self.reset()

    def set_config(self, matrix=None, flat=None):
        Board.validate(matrix=matrix, flat=flat)
        self.matrix = matrix or Board.to_matrix(flat=flat)

    def reset(self):
        self.matrix = self.to_matrix(conf.INITIAL_BOARD)

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

    def __str__(self):
        header = footer = "\n%s%s%s\n" %("+--", " --"*6, " --+")
        board = '\n'.join(["%s%s %s" % ('|', '  '.join(i), '|')
                           for i in self.matrix])
        return header + board + footer

