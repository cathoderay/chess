import unittest

from board import Board


class BoardTest(unittest.TestCase):
    def test_starting_board(self):
        matrix = ['R N B Q K B N R',
                  'P P P P P P P P',
                  '_ _ _ _ _ _ _ _',
                  '_ _ _ _ _ _ _ _',
                  '_ _ _ _ _ _ _ _',
                  '_ _ _ _ _ _ _ _',
                  'p p p p p p p p',
                  'r n b q k b n r']
        expected = map(lambda x: x.split(' '), matrix) 
        result = Board().matrix
        self.assertEqual(expected, result)
        

if __name__ == '__main__':
    unittest.main()
