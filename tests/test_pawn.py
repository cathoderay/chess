from mock import patch
import unittest

import conf
from board import Board
from square import Square
from pawn import Pawn


class PawnTest(unittest.TestCase):
    @patch('piece.Piece.__init__')
    def test_calls_super_in_init(self, init):
        pawn = Pawn(Board(), square=Square(1, 1), color=conf.BLACK)
        assert init.called

    @patch('board.Board.notify_move')
    def test_move_forward_black(self, notify):
        pawn = Pawn(Board(), square=Square(1, 1), color=conf.BLACK)
        pawn.move_forward()
        expected = Square(2, 1)
        result = pawn.square
        self.assertEqual(expected, result)
        assert notify.called

    @patch('board.Board.notify_move')
    def test_move_forward_white(self, notify):
        pawn = Pawn(Board(), square=Square(6, 3), color=conf.WHITE)
        pawn.move_forward()
        expected = Square(5, 3)
        result = pawn.square
        self.assertEqual(expected, result)
        assert notify.called


    #def test_legal_moves(self):
    #    pawn = Pawn(Board(), square=Square(6, 0), color=conf.WHITE)
    #    expected = [Square(5, 0), Square(4, 0)]
    #    result = pawn.legal_moves()
    #    self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
