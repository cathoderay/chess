import unittest

from square import Square


class SquareTest(unittest.TestCase):

    def test_north_returns_none(self):
        expected = None
        result = Square(0, 0).north()
        self.assertEqual(expected, result)

    def test_north(self):
        expected = Square(0, 1)
        result = Square(1, 1).north()
        self.assertEqual(expected, result)

    def test_south_returns_none(self):
        expected = None
        result = Square(7, 7).south()
        self.assertEqual(expected, result)

    def test_south(self):
        expected = Square(2, 1)
        result = Square(1, 1).south()
        self.assertEqual(expected, result)

    def test_west_returns_none(self):
        expected = None
        result = Square(0, 0).west()
        self.assertEqual(expected, result)

    def test_west(self):
        expected = Square(1, 0)
        result = Square(1, 1).west()
        self.assertEqual(expected, result)

    def test_east_returns_none(self):
        expected = None
        result = Square(7, 7).east()
        self.assertEqual(expected, result)

    def test_east(self):
        expected = Square(1, 2)
        result = Square(1, 1).east()
        self.assertEqual(expected, result)

    def test_northeast_returns_none(self):
        expected = None
        result = Square(0, 7).northeast()
        self.assertEqual(expected, result)

    def test_northeast(self):
        expected = Square(0, 2)
        result = Square(1, 1).northeast()
        self.assertEqual(expected, result)

    def test_northwest_returns_none(self):
        expected = None
        result = Square(0, 0).northwest()
        self.assertEqual(expected, result)

    def test_northwest(self):
        expected = Square(0, 0)
        result = Square(1, 1).northwest()
        self.assertEqual(expected, result)

    def test_southeast_returns_none(self):
        expected = None
        result = Square(7, 7).southeast()
        self.assertEqual(expected, result)

    def test_southeast(self):
        expected = Square(2, 2)
        result = Square(1, 1).southeast()
        self.assertEqual(expected, result)

    def test_southwest_returns_none(self):
        expected = None
        result = Square(7, 0).southwest()
        self.assertEqual(expected, result)

    def test_southwest(self):
        expected = Square(2, 0)
        result = Square(1, 1).southwest()
        self.assertEqual(expected, result)

    def test_norths(self):
        expected = [Square(5, 0), Square(4, 0), Square(3, 0),
                    Square(2, 0), Square(1, 0), Square(0, 0)]

        result = Square(6, 0).norths()
        self.assertEqual(expected, result)

    def test_souths(self):
        expected = [Square(1, 3), Square(2, 3), Square(3, 3),
                    Square(4, 3), Square(5, 3), Square(6, 3),
                    Square(7, 3)]
        result = Square(0, 3).souths()
        self.assertEqual(expected, result)

    def test_wests(self):
        expected = [Square(0, 6), Square(0, 5), Square(0, 4),
                    Square(0, 3), Square(0, 2), Square(0, 1),
                    Square(0, 0)]
        result = Square(0, 7).wests()
        self.assertEqual(expected, result)

    def test_easts(self):
        expected = [Square(0, 1), Square(0, 2), Square(0, 3),
                    Square(0, 4), Square(0, 5), Square(0, 6),
                    Square(0, 7)]
        result = Square(0, 0).easts()
        self.assertEqual(expected, result)

    def test_northeasts(self):
        expected = [Square(6, 1), Square(5, 2), Square(4, 3),
                    Square(3, 4), Square(2, 5), Square(1, 6),
                    Square(0, 7)]
        result = Square(7, 0).northeasts()
        self.assertEqual(expected, result)

    def test_northwests(self):
        expected = [Square(6, 6), Square(5, 5), Square(4, 4),
                    Square(3, 3), Square(2, 2), Square(1, 1),
                    Square(0, 0)]
        result = Square(7, 7).northwests()
        self.assertEqual(expected, result)

    def test_southeasts(self):
        expected = [Square(1, 1), Square(2, 2), Square(3, 3),
                    Square(4, 4), Square(5, 5), Square(6, 6),
                    Square(7, 7)]
        result = Square(0, 0).southeasts()
        self.assertEqual(expected, result)

    def test_southwests(self):
        expected = [Square(1, 6), Square(2, 5), Square(3, 4),
                    Square(4, 3), Square(5, 2), Square(6, 1),
                    Square(7, 0)]
        result = Square(0, 7).southwests()
        self.assertEqual(expected, result)

    def test_sub_overload_with_tuple(self):
        expected = Square(0, 0)
        result = Square(1, 2) - (1, 2)
        self.assertEqual(expected, result)

    def test_add_overload_with_tuple(self):
        expected = Square(7, 7)
        result = Square(0, 0) + (7, 7)
        self.assertEqual(expected, result)

    def test_repr(self):
        expected = "Square(4, 2)"
        result = str(Square(4, 2))
        self.assertEqual(expected, result)
