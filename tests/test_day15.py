import unittest
from day_15 import *

test_board = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

class DayFifteenTest(unittest.TestCase):

    def test_parsing_board(self):
        board = read_board(test_board)
        self.assertEqual(board[(0, 0)], 1)
        self.assertEqual(board[(4, 2)], 6)