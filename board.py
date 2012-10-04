import conf


class Board:
    def __init__(self):
        self.matrix = self.to_matrix(conf.INITIAL_BOARD)

    def set_config(self, matrix):
        self.matrix = matrix

    def to_flat(self, matrix=None):
        matrix = matrix or self.matrix
        return ''.join([e for l in matrix
                          for e in l])

    @classmethod
    def to_matrix(self, flat):
        return [list(flat[l*8:l*8+8])
                for l in xrange(8)]
