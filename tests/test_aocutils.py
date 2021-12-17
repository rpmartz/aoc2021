import unittest

from aocutils import Point, get_neighbors


class AocUtilsTest(unittest.TestCase):

    def test_four_neighbors(self):
        point = Point(x=3, y=4)

        expected = {Point(3, 3), Point(3, 5), Point(2, 4), Point(4, 4)}
        actual = get_neighbors(point, 4)

        self.assertEqual(expected, actual)

    def test_eight_neighbors(self):
        point = Point(x=3, y=4)

        expected = {
            Point(3, 3), Point(3, 5), Point(2, 4), Point(4, 4),
            Point(2, 3), Point(2, 5), Point(4, 3), Point(4, 5)
        }

        actual = get_neighbors(point, num=8)
        self.assertEqual(expected, actual)
