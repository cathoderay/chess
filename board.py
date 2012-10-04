import conf
from exception import InvalidBoard


class Board:
    valid = set('rRnNbBqQkKpP_')

    def __init__(self):
        self.reset()

    def set_config(self, matrix=None, flat=None):
        self.matrix = matrix or self.to_matrix(flat)

    def reset(self):
        self.matrix = self.to_matrix(conf.INITIAL_BOARD)

    def to_flat(self, matrix=None):
        matrix = matrix or self.matrix
        return ''.join([e for l in matrix
                          for e in l])

    @classmethod
    def to_matrix(self, flat):
        return [list(flat[l*8:l*8+8])
                for l in xrange(8)]

    @classmethod
    def validate(self, flat=None):
        if len(flat) != 64 or not \
           set(flat).issubset(self.valid):
            raise InvalidBoard
