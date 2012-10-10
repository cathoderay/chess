from mock import MagicMock
import unittest

import conf
from piece import Piece
from board import Board
from square import Square


class PieceTest(unittest.TestCase):
    def test_has_moved(self):
        expected = False
        result = Piece().has_moved
        self.assertEqual(expected, result)

    def test_instantiate_with_a_board(self):
        board = Board()
        piece = Piece(board)
        expected = board
        result = piece.board
        self.assertEqual(expected, result)

    def test_instantiate_within_square(self):
        square = Square(7, 4)
        piece = Piece(square=square)
        expected = square
        result = piece.square
        self.assertEqual(expected, result)

    def test_instantiate_with_color(self):
        piece = Piece(color=conf.WHITE)
        expected = conf.WHITE
        result = piece.color
        self.assertEqual(expected, result)

    def test_opposite_color(self):
        piece = Piece(color=conf.WHITE)
        expected = conf.BLACK
        result = piece.opposite_color
        self.assertEqual(expected, result)

    def test_is_valid(self):
        piece = Piece()
        piece.valid_moves = MagicMock(return_value=[Square(4, 2)])
        expected = True
        result = piece.is_valid(Square(4, 2))
        self.assertEqual(expected, result)

    def test_is_not_valid(self):
        piece = Piece()
        piece.valid_moves = MagicMock(return_value=[])
        expected = False
        result = piece.is_valid(Square(4, 2))
        self.assertEqual(expected, result)

    def test_valid_moves_raises_not_implemented_error(self):
        piece = Piece()
        self.assertRaises(NotImplementedError, piece.valid_moves)
