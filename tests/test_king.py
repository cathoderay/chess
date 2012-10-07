from mock import patch
import unittest

from conf import WHITE, EMPTY, BLACK
from square import Square
from king import King
from board import Board


class KingTest(unittest.TestCase):
    @patch('piece.Piece.__init__')
    def test_calls_super_in_init(self, init):
        king = King(Board(), Square(4, 2), WHITE)
        assert init.called

    def test_valid_moves_initial_position(self):
        king = King(Board(), Square(7, 4), WHITE)
        expected = []
        result = king.valid_moves()
        self.assertEqual(expected, result)

    def test_valid_moves_clean_board(self):
        board = Board()
        board.clean()
        king = King(board, Square(4, 4), BLACK)
        expected = [Square(3, 3), Square(3, 4), Square(3, 5),
                    Square(4, 3), Square(4, 5),
                    Square(5, 3), Square(5, 4), Square(5, 5)]
        result = king.valid_moves()
        self.assertEqual(expected, result)

    def test_valid_moves_border(self):
        board = Board()
        board.clean()
        king = King(board, Square(0, 0), BLACK)
        expected = [Square(0, 1), Square(1, 0), Square(1, 1)]
        result = king.valid_moves()
        self.assertEqual(expected, result)

    def test_attacks_north(self):
        board = Board()
        board.clean() 
        board.matrix[3][2] = "P"
        king = King(board, Square(4, 2), WHITE)
        expected = [Square(3, 2)]
        result = king.attacking_moves()
        self.assertEqual(expected, result)

    def test_valid_moves_with_other_pieces(self):
        board = Board()
        board.clean()
        board.matrix[1][1] = 'P'
        board.matrix[1][2] = 'P'
        board.matrix[2][3] = 'b'
        king = King(board, Square(2, 2), WHITE)
        expected = [Square(1, 3), Square(2, 1), Square(3, 1), 
                    Square(3, 2),Square(3, 3), Square(1, 1),
                    Square(1, 2)]
        result = king.valid_moves()
        self.assertEqual(expected, result)

