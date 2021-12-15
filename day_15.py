from collections import defaultdict


def read_board(board_as_string: str):
    board = defaultdict(int)
    for i, row in enumerate(board_as_string.splitlines()):
        for j, char in enumerate(row):
            board[i, j] = int(char)

    return board