from mock import patch
import unittest

import conf
from square import Square
from king import King
from board import Board


class KingTest(unittest.TestCase):
    @patch('piece.Piece.__init__')
    def test_calls_super_in_init(self, init):
        king = King(Board(), Square(4, 2), conf.WHITE)
        assert init.called

    def test_valid_moves_initial_position(self):
        king = King(Board(), Square(4, 2), conf.WHITE)
        expected = []
        result = king.valid_moves()
        self.assertEqual(expected, result)

