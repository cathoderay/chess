import unittest

import conf
from board import Board


class BoardTest(unittest.TestCase):
    def test_starting_board(self):
        expected = Board.to_matrix(conf.INITIAL_BOARD)
        result = Board().matrix
        self.assertEqual(expected, result)

    def test_set_config(self):
        matrix = Board.to_matrix('RNBQKBNRPPPPPPPP____________________p___________pppp_ppprnbqkbnr')
        b = Board()
        b.set_config(matrix)
        expected = matrix
        result = b.matrix
        self.assertEqual(expected, result)

    def test_from_matrix_to_flat_string(self):
        expected = conf.INITIAL_BOARD
        b = Board()
        result = b.to_flat()
        self.assertEqual(expected, result)

    def test_from_flat_string_to_matrix(self):
        flat = "RNBQKBNRPPPPPPPP____________________p___________pppp_ppprnbqkbnr"
        matrix = ['R N B Q K B N R',
                  'P P P P P P P P',
                  '_ _ _ _ _ _ _ _',
                  '_ _ _ _ _ _ _ _',
                  '_ _ _ _ p _ _ _',
                  '_ _ _ _ _ _ _ _',
                  'p p p p _ p p p',
                  'r n b q k b n r']
        expected = map(lambda x: x.split(' '), matrix)
        result = Board.to_matrix(flat)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
