from mock import patch
import unittest

from conf import WHITE
from square import Square
from board import Board
from rook import Rook


class RookTest(unittest.TestCase):
    @patch('piece.Piece.__init__')
    def test_calls_super_in_init(self, init):
        rook = Rook(Board(), Square(4, 2), WHITE)
        assert init.called

    def test_valid_moves_clean_board(self):
        b = Board()
        b.clean()
        rook = Rook(b, Square(4, 2), WHITE)
        expected = [Square(3, 2), Square(2, 2), Square(1, 2),
                    Square(0, 2), Square(5, 2), Square(6, 2),
                    Square(7, 2), Square(4, 1), Square(4, 0),
                    Square(4, 3), Square(4, 4), Square(4, 5),
                    Square(4, 6), Square(4, 7)]
        result = rook.valid_moves()
        self.assertEqual(expected, result)
