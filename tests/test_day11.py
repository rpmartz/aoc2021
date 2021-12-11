import unittest

from day_11 import *

board = [
    [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
    [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
    [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
    [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
    [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
    [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
    [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
    [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
    [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
    [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]
]

class DayEleven(unittest.TestCase):

    def test_example(self):

        expected = 1656
        actual = count_num_flashes(board, 100)

        self.assertEqual(expected, actual)

    def test_sub_example(self):
        subsample_board = [
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1]
        ]

        count_num_flashes(subsample_board, 1)
        for row in subsample_board:
            print(row)

    def test_get_neighbors_upper_left(self):
        neighbors = get_neighbors(board, 0, 0)
        self.assertEqual(len(neighbors), 3)

        expected = {(0, 1), (1, 0), (1, 1)}
        self.assertEqual(expected, neighbors)

    def test_get_neighbors_upper_right(self):
        neighbors = get_neighbors(board, 0, 9)
        self.assertEqual(len(neighbors), 3)

        expected = {(0, 8), (1, 8), (1, 9)}
        self.assertEqual(expected, neighbors)

    def test_get_neighbors_lower_left(self):
        neighbors = get_neighbors(board, 9, 0)
        self.assertEqual(len(neighbors), 3)

        expected = {(9, 1), (8, 0), (8, 1)}
        self.assertEqual(expected, neighbors)

    def test_get_neighbors_lower_right(self):
        neighbors = get_neighbors(board, 9, 9)
        self.assertEqual(len(neighbors), 3)

        expected = {(9, 8), (8, 8), (8, 9)}
        self.assertEqual(expected, neighbors)

    def test_get_neighbors_middle(self):
        neighbors = get_neighbors(board, 2, 3)
        self.assertEqual(len(neighbors), 8)

        expected = {(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)}
        self.assertEqual(expected, neighbors)

    def test_get_neighbors_top_middle(self):
        neighbors = get_neighbors(board, 0, 3)
        self.assertEqual(len(neighbors), 5)

        expected = {(0, 2), (0, 4), (1, 2), (1, 3), (1, 4)}
        self.assertEqual(expected, neighbors)

    def test_get_neighbors_bottom_middle(self):
        neighbors = get_neighbors(board, 9, 3)
        self.assertEqual(len(neighbors), 5)

        expected = {(9, 2), (9, 4), (8, 2), (8, 3), (8, 4)}
        self.assertEqual(expected, neighbors)
