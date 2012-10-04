import conf


class Board:
    def __init__(self):
        self.matrix = self.from_flat(conf.INITIAL_BOARD)

    def set_config(self, matrix):
        self.matrix = matrix

    def to_flat(self, matrix=None):
        matrix = matrix or self.matrix
        return ''.join([e for l in matrix
                          for e in l])

    def from_flat(self, flat):
        return [list(flat[l*8:l*8+8])
                for l in xrange(8)]
