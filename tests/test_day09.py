import unittest

from day_09 import *


class DayNineTest(unittest.TestCase):

    def test_find_low_points_from_sample_board(self):
        board = [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
        ]

        low_points = find_low_points(board)
        expected = [(0, 1, 1), (0, 9, 0), (2, 2, 5), (4, 6, 5)]
        self.assertEqual(low_points, expected)

    def test_summing_risk_score(self):
        low_points = [(0, 1, 1), (0, 9, 0), (2, 2, 5), (4, 6, 5)]
        self.assertEqual(15, calculate_risk_level(low_points))
