import unittest

import conf
from board import Board
from exception import InvalidBoard


class BoardTest(unittest.TestCase):
    def test_starting_board(self):
        expected = Board.to_matrix(conf.INITIAL_BOARD)
        result = Board().matrix
        self.assertEqual(expected, result)

    def test_set_config_from_matrix(self):
        flat = 'RNBQKBNRPPPPPPPP____________________p___________pppp_ppprnbqkbnr'
        matrix = Board.to_matrix(flat)

        b = Board()
        b.set_config(matrix=matrix)

        expected = matrix
        result = b.matrix
        self.assertEqual(expected, result)

    def test_set_config_from_flat(self):
        flat = 'RNBQKBNRPPPPPPPP____________________p___________pppp_ppprnbqkbnr'

        b = Board()
        b.set_config(flat=flat)

        expected = Board.to_matrix(flat)
        result = b.matrix
        self.assertEqual(expected, result)

    def test_from_matrix_to_flat_string(self):
        expected = conf.INITIAL_BOARD
        result = Board().to_flat()
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

    def test_reset_board(self):
        flat = "RNBQKBNRPPPPPPPP____________________pp___________pppp__pprnbqkbnr"
        some_config = Board.to_matrix(flat)

        b = Board()
        b.set_config(some_config)
        self.assertEqual(some_config, b.matrix)

        b.reset()

        expected = Board.to_matrix(conf.INITIAL_BOARD)
        result = b.matrix
        self.assertEqual(expected, result)

    def test_flat_wrong_number_of_places(self):
        flat = "rrrRRR"
        self.assertRaises(InvalidBoard, Board.validate, {'flat': flat})


if __name__ == '__main__':
    unittest.main()
