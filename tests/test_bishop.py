from mock import patch
import unittest

from conf import WHITE
from square import Square
from bishop import Bishop
from board import Board


class BishopTest(unittest.TestCase):
    @patch('piece.Piece.__init__')
    def test_calls_super_in_init(self, init):
        bishop = Bishop(Board(), Square(4, 2), WHITE)
        assert init.called


