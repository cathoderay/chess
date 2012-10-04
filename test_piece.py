import unittest

import conf
from piece import Piece
from board import Board


class PieceTest(unittest.TestCase):
    def test_have_moved(self):
        expected = False
        result = Piece().have_moved
        self.assertEqual(expected, result)

    def test_instantiate_with_a_board(self):
        board = Board()
        piece = Piece(board)

        expected = board
        result = piece.board
        self.assertEqual(expected, result)

    def test_current_position(self):
        piece = Piece(position=(7, 4))
        expected = (7, 4)
        result = piece.position
        self.assertEqual(expected, result)

    def test_color(self):
        piece = Piece(color=conf.WHITE)
        expected = conf.WHITE
        result = piece.color
        self.assertEqual(expected, result)

    def test_raise_exceptions_for_not_implemented(self):
        piece = Piece()
        self.assertRaises(NotImplementedError, piece.is_legal, None)
        self.assertRaises(NotImplementedError, piece.legal_moves)


if __name__ == '__main__':
    unittest.main()

