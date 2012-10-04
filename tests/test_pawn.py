from mock import patch
import unittest

import conf
from board import Board
from pawn import Pawn


class PawnTest(unittest.TestCase):
    @patch('piece.Piece.__init__')
    def test_calls_super_in_init(self, init):
        pawn = Pawn(Board(), position=(1, 1), color=conf.WHITE)
        assert init.called
        
        


if __name__ == '__main__':
    unittest.main()
