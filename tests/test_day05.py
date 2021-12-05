from unittest import TestCase

from day_05 import build_board, part_one


class Day05Tests(TestCase):

    def test_horizontal_line_with_two_segments(self):
        board = build_board(10, 10)
        lines = ['0,9 -> 5,9', '0,9 -> 2,9']

        part_one(lines, board)
        for row in board:
            print(row)

        self.assertEqual(board[9][0], 2)
        self.assertEqual(board[9][1], 2)
        self.assertEqual(board[9][2], 2)
        self.assertEqual(board[9][3], 1)
        self.assertEqual(board[9][4], 1)
        self.assertEqual(board[9][5], 1)
