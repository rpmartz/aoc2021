import unittest
from day_15 import *

test_board = """\

from aocutils import read_numeric_grid
from day_15 import calculate_min_risk

example_input = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


class DayFifteenTest(unittest.TestCase):

    def test_problem_example_risk_score(self):
        expected = 40
        actual = calculate_min_risk(read_numeric_grid(example_input))

        self.assertEqual(expected, actual)
