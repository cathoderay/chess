import conf
from exception import InvalidBoard


class Board:
    valid = set('rRnNbBqQkKpP_')

    def __init__(self):
        self.reset()

    def set_config(self, matrix=None, flat=None):
        Board.validate(matrix=matrix, flat=flat)
        self.matrix = matrix or Board.to_matrix(flat)

    def reset(self):
        self.matrix = Board.to_matrix(conf.INITIAL_BOARD)

    def move(self, a, b):
        piece = self.matrix[a[0]][a[1]]
        self.matrix[a[0]][a[1]] = conf.BLANK
        self.matrix[b[0]][b[1]] = piece

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
        try:
            flat = flat or Board.to_flat(matrix)
        except:
            raise InvalidBoard
        if len(flat) != 64 or not \
           set(flat).issubset(self.valid):
            raise InvalidBoard

    def __str__(self):
        header = footer = "\n%s%s%s\n" %("+--", " --"*6, " --+")
        board = '\n'.join(["%s%s %s" % ('|', '  '.join(l), '|')
                           for l in self.matrix])
        return header + board + footer


if __name__ == '__main__':
    # usage examples
    b = Board()
    print b

    b.set_config(flat="_"*63 + "R")
    print b

    b.move((7, 7), (0, 7))
    print b

    b.reset()
    print b

