import unittest
from mock import patch

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
        matrix = Board.to_matrix(flat)

        b = Board()
        b.set_config(flat=flat)

        expected = matrix
        result = b.matrix
        self.assertEqual(expected, result)

    def test_to_flat(self):
        matrix = ['R N B Q K B N R',
                  'P P P P P P P P',
                  '_ _ _ _ _ _ _ _',
                  '_ _ _ _ _ _ _ _',
                  '_ _ _ _ _ _ _ _',
                  '_ _ _ _ _ _ _ _',
                  'p p p p p p p p',
                  'r n b q k b n r']
        matrix = map(lambda x: x.split(' '), matrix)

        expected = conf.INITIAL_BOARD
        result = Board.to_flat(matrix)
        self.assertEqual(expected, result)

    def test_to_matrix(self):
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

    def test_reset(self):
        flat = "RNBQKBNRPPPPPPPP____________________pp___________pppp__pprnbqkbnr"
        matrix = Board.to_matrix(flat)
        b = Board()
        b.set_config(matrix=matrix)

        b.reset()

        expected = Board.to_matrix(conf.INITIAL_BOARD)
        result = b.matrix
        self.assertEqual(expected, result)

    def test_invalid_number_of_places_raises_exception(self):
        flat = "rrrRRR"
        self.assertRaises(InvalidBoard, Board.validate, flat=flat)

    def test_invalid_chars_raises_exception(self):
        flat = "_"*63 + "x"
        self.assertRaises(InvalidBoard, Board.validate, flat=flat)

    def test_invalid_matrix_raises_exception(self):
        matrix = [["gotcha"]]
        self.assertRaises(InvalidBoard, Board.validate, matrix=matrix)

    @patch('board.Board.validate')
    def test_validation_is_done_when_set_config(self, validate):
        flat = "RNBQKBNRPPPPPPPP____________________pp___________pppp__pprnbqkbnr"

        b = Board()
        b.set_config(flat=flat)

        assert validate.called

    def test_string_representation(self):
        expected = """
+-- -- -- -- -- -- -- --+
|R  N  B  Q  K  B  N  R |
|P  P  P  P  P  P  P  P |
|_  _  _  _  _  _  _  _ |
|_  _  _  _  _  _  _  _ |
|_  _  _  _  _  _  _  _ |
|_  _  _  _  _  _  _  _ |
|p  p  p  p  p  p  p  p |
|r  n  b  q  k  b  n  r |
+-- -- -- -- -- -- -- --+
"""
        result = str(Board())
        self.assertEqual(expected, result)

    def test_move(self):
        b = Board()
        b.move((6, 0), (4, 0))
        self.assertEqual(b.matrix[6][0], conf.EMPTY)
        self.assertEqual(b.matrix[4][0], "p")

    def test_is_empty(self):
        b = Board()
        expected = False
        result = b.is_empty((0, 0))
        self.assertEqual(expected, result)

        expected = True
        result = b.is_empty((3,3))
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
