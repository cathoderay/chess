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

    def test_valid_moves_initial_position_white(self):
        pawn = Pawn(Board(), square=Square(6, 3), color=conf.WHITE)
        expected = [Square(5, 3), Square(4, 3)]
        result = pawn.valid_moves()
        self.assertEqual(expected, result)
        
    def test_valid_moves_initial_position_black(self):
        pawn = Pawn(Board(), square=Square(1, 3), color=conf.BLACK)
        expected = [Square(2, 3), Square(3, 3)]
        result = pawn.valid_moves()
        self.assertEqual(expected, result)

    def test_valid_moves_seventh_row_white(self):
        board = Board()
        board.set_config(flat="_"*64) # it doesn't matter much
        pawn = Pawn(board, square=Square(1, 0), color=conf.WHITE)
        expected = [Square(0, 0)]
        result = pawn.valid_moves()
        self.assertEqual(expected, result)
       
    def test_valid_moves_second_row_black(self):
        board = Board()
        board.set_config(flat="_"*64) # it doesn't matter much
        pawn = Pawn(board, square=Square(6, 0), color=conf.BLACK)
        expected = [Square(7, 0)]
        result = pawn.valid_moves()
        self.assertEqual(expected, result)
        

if __name__ == '__main__':
    unittest.main()
