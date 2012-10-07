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
