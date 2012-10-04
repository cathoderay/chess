import unittest

from exception import OutOfBoard
from square import Square


class SquareTest(unittest.TestCase):

    def test_up_raises_exception(self):
        self.assertRaises(OutOfBoard, Square(0, 0).up)

    def test_up(self):
        square = Square(1, 1)
        expected = Square(0, 1)
        result = square.up()
        self.assertEqual(expected, result)

    def test_down_raises_exception(self):
        self.assertRaises(OutOfBoard, Square(7, 7).down)

    def test_down(self):
        square = Square(1, 1)
        expected = Square(2, 1)
        result = square.down()
        self.assertEqual(expected, result)

    def test_left_raises_exception(self):
        self.assertRaises(OutOfBoard, Square(0, 0).left)

    def test_left(self):
        square = Square(1, 1)
        expected = Square(1, 0)
        result = square.left()
        self.assertEqual(expected, result)

    def test_right_raises_exception(self):
        self.assertRaises(OutOfBoard, Square(7, 7).right)

    def test_right(self):
        square = Square(1, 1)
        expected = Square(1, 2)
        result = square.right()
        self.assertEqual(expected, result)

    def test_northeast_raises_exception(self):
        self.assertRaises(OutOfBoard, Square(0, 7).northeast)

    def test_northeast(self):
        square = Square(1, 1)
        expected = Square(0, 2)
        result = square.northeast()
        self.assertEqual(expected, result)

    def test_northwest_raises_exception(self):
        self.assertRaises(OutOfBoard, Square(0, 0).northwest)

    def test_northwest(self):
        square = Square(1, 1)
        expected = Square(0, 0)
        result = square.northwest()
        self.assertEqual(expected, result)

    def test_southeast_raises_exception(self):
        self.assertRaises(OutOfBoard, Square(7, 7).southeast)

    def test_southeast(self):
        square = Square(1, 1)
        expected = Square(2, 2)
        result = square.southeast()
        self.assertEqual(expected, result)

    def test_southwest_raises_exception(self):
        self.assertRaises(OutOfBoard, Square(7, 0).southwest)

    def test_southwest(self):
        square = Square(1, 1)
        expected = Square(2, 0)
        result = square.southwest()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
