import unittest

import conf
from piece import Piece
from board import Board
from square import Square
from exception import OutOfBoard


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


if __name__ == '__main__':
    unittest.main()
