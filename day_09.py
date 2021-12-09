from typing import List


def read_board():
    with open('data/day09.txt', 'r') as f:
        board = []
        for line in f.readlines():
            board.append([int(num) for num in line.strip()])

    return board


def find_low_points(board):
    board_depth = len(board) - 1
    board_width = len(board[0]) - 1

    low_points = []
    for i, row in enumerate(board):
        for j, _ in enumerate(row):

            lt_left = (j - 1 < 0) or row[j] < row[j - 1]
            lt_right = (j + 1 > board_width) or row[j] < row[j + 1]
            lt_bottom = (i + 1 > board_depth) or row[j] < board[i + 1][j]
            lt_top = (i - 1 < 0) or row[j] < board[i - 1][j]

            if all([lt_left, lt_right, lt_top, lt_bottom]):
                low_points.append((i, j, row[j]))

    return low_points


def calculate_risk_level(low_points):
    return sum(1 + p[2] for p in low_points)


def get_coordinates_of_neighbors(x, y, board):
    neighbors = []

    # left neighbor
    if x > 0:
        neighbors.append((x - 1, y))

    # right
    if x + 1 < len(board[0]) - 1:
        neighbors.append((x + 1, y))

    # top
    if y > 0:
        neighbors.append((x, y - 1))
    # bottom
    if y + 1 < len(board) - 1:
        neighbors.append((x, y + 1))

    return neighbors


def find_basin_sizes(low_points, board) -> List[int]:
    for point in low_points:
        x, y = point[0], point[1]


def do_part_one():
    board = read_board()
    low_points = find_low_points(board)
    risk_level = calculate_risk_level(low_points)

    print('Pt 1: %s' % risk_level)


def do_part_two():
    board = read_board()
    low_points = find_low_points(board)
    basins = find_basin_sizes(low_points, board)


if __name__ == '__main__':
    do_part_one()
    do_part_two()
