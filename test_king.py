import unittest

from king import King


class KingTest(unittest.TestCase):
    def test_have_moved(self):
        expected = False
        result = King().have_moved
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

