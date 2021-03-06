import unittest
from mock import patch

from conf import EMPTY, INITIAL_BOARD, BLACK, WHITE
from board import Board
from exception import InvalidBoard


class BoardTest(unittest.TestCase):
    def test_starting_board(self):
        expected = Board.to_matrix(INITIAL_BOARD)
        result = Board().matrix
        self.assertEqual(expected, result)

    def test_set_config_from_matrix(self):
        flat = 'RNBQKBNRPPPPPPPP....................p...........pppp.ppprnbqkbnr'
        matrix = Board.to_matrix(flat)

        b = Board()
        b.set_config(matrix=matrix)

        expected = matrix
        result = b.matrix
        self.assertEqual(expected, result)

    def test_set_config_from_flat(self):
        flat = 'RNBQKBNRPPPPPPPP....................p...........pppp.ppprnbqkbnr'
        matrix = Board.to_matrix(flat)

        b = Board()
        b.set_config(flat=flat)

        expected = matrix
        result = b.matrix
        self.assertEqual(expected, result)

    def test_to_flat(self):
        matrix = ['R N B Q K B N R',
                  'P P P P P P P P',
                  '. . . . . . . .',
                  '. . . . . . . .',
                  '. . . . . . . .',
                  '. . . . . . . .',
                  'p p p p p p p p',
                  'r n b q k b n r']
        matrix = map(lambda x: x.split(' '), matrix)

        expected = INITIAL_BOARD
        result = Board.to_flat(matrix)
        self.assertEqual(expected, result)

    def test_to_matrix(self):
        flat = "RNBQKBNRPPPPPPPP....................p...........pppp.ppprnbqkbnr"
        matrix = ['R N B Q K B N R',
                  'P P P P P P P P',
                  '. . . . . . . .',
                  '. . . . . . . .',
                  '. . . . p . . .',
                  '. . . . . . . .',
                  'p p p p . p p p',
                  'r n b q k b n r']

        expected = map(lambda x: x.split(' '), matrix)
        result = Board.to_matrix(flat)
        self.assertEqual(expected, result)

    def test_reset(self):
        flat = "RNBQKBNRPPPPPPPP....................pp...........pppp..pprnbqkbnr"
        matrix = Board.to_matrix(flat)
        b = Board()
        b.set_config(matrix=matrix)

        b.reset()

        expected = Board.to_matrix(INITIAL_BOARD)
        result = b.matrix
        self.assertEqual(expected, result)

    def test_invalid_number_of_places_raises_exception(self):
        flat = "rrrRRR"
        self.assertRaises(InvalidBoard, Board.validate, flat=flat)

    def test_invalid_chars_raises_exception(self):
        flat = EMPTY*63 + "x"
        self.assertRaises(InvalidBoard, Board.validate, flat=flat)

    def test_invalid_matrix_raises_exception(self):
        matrix = [["gotcha"]]
        self.assertRaises(InvalidBoard, Board.validate, matrix=matrix)

    @patch('board.Board.validate')
    def test_validation_is_done_when_set_config(self, validate):
        flat = EMPTY*64

        b = Board()
        b.set_config(flat=flat)

        assert validate.called

    def test_string_representation(self):
        expected = """
  .- - - - - - - -.
8 |R N B Q K B N R|
7 |P P P P P P P P|
6 |. . . . . . . .|
5 |. . . . . . . .|
4 |. . . . . . . .|
3 |. . . . . . . .|
2 |p p p p p p p p|
1 |r n b q k b n r|
  .- - - - - - - -.
   a b c d e f g h
"""
        result = str(Board())
        self.assertEqual(expected, result)

    def test_move(self):
        b = Board()
        b.move((6, 0), (4, 0))
        self.assertEqual(b.matrix[6][0], EMPTY)
        self.assertEqual(b.matrix[4][0], "p")

    def test_is_empty(self):
        b = Board()
        expected = False
        result = b.is_empty((0, 0))
        self.assertEqual(expected, result)

        expected = True
        result = b.is_empty((3,3))
        self.assertEqual(expected, result)

    def test_is_black(self):
        b = Board()
        expected = True
        result = b.is_black((0, 0))
        self.assertEqual(expected, result)

    def test_is_white(self):
        b = Board()
        expected = True
        result = b.is_white((6, 6))
        self.assertEqual(expected, result)

    def test_color_black(self):
        b = Board()
        expected = BLACK
        result = b.color((0, 0))
        self.assertEqual(expected, result)

    def test_color_white(self):
        b = Board()
        expected = WHITE
        result = b.color((7, 7))
        self.assertEqual(expected, result)

    def test_color_none(self):
        b = Board()
        expected = None
        result = b.color((4, 4))
        self.assertEqual(expected, result)

    def test_clean(self):
        b = Board()
        expected = 64
        b.clean()
        result = b.to_flat(b.matrix).count(EMPTY)
        self.assertEqual(expected, result)
