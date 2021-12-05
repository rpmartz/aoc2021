from collections import namedtuple

Point = namedtuple("Point", "x y")


def read_file():
    with open('data/day05_test.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def build_board(rows, columns):
    """
    build 1000 x 1000 board of zeros
    """
    board = list()
    for i in range(0, rows):
        row = []
        for j in range(0, columns):
            row.append(0)

        board.append(row)

    return board


def mark_horizontal_line(board, start: Point, end: Point):
    assert start.y == end.y
    for column in range(start.x, start.x + 1):
        board[start.y][column] = board[start.y][column] + 1


def mark_vertical_line(board, start: Point, end: Point):
    assert start.x == end.x
    for row in range(start.y, end.y + 1):
        board[row][start.x] = board[row][start.x] + 1


def part_one(lines, board):
    for line in lines:
        both_coordinate_pairs = line.split('->')
        first_pair = both_coordinate_pairs[0].split(',')
        second_pair = both_coordinate_pairs[1].split(',')

        start = Point(int(first_pair[0]), int(first_pair[1]))
        end = Point(int(second_pair[0]), int(second_pair[1]))

        is_horizontal = start.y == end.y
        is_vertical = start.x == end.x
        if is_vertical:
            mark_vertical_line(board, start, end)
        elif is_horizontal:
            mark_horizontal_line(board, start, end)
        else:
            continue


if __name__ == '__main__':
    lines = read_file()
    board = build_board(10, 10)

    for row in board:
        print(row)
