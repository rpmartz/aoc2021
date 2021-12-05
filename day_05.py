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


def mark_horizontal_line(board, row, y1, y2):
    for idx in range(y1, y2 + 1):
        current_val = board[row][idx]
        board[row][idx] = current_val + 1

def mark_vertical_line(board, column, x1, x2):
    for idx in range(x1, x2):
        current_val = board[idx][column]
        board[idx][column] = current_val

def mark_segments(x1, y1, x2, y2, board):
    is_horizontal_line = x1 == x2
    if is_horizontal_line:
        mark_horizontal_line(board, x1, y1, y2)
    else:
        mark_vertical_line(board, y1, x1, x2)


if __name__ == '__main__':
    lines = read_file()
    board = build_board(10, 10)

    for line in lines:
        both_coordinate_pairs = line.split('->')
        first_pair = both_coordinate_pairs[0].split(',')
        second_pair = both_coordinate_pairs[1].split(',')

        x1 = int(first_pair[0])
        y1 = int(first_pair[1])

        x2 = int(second_pair[0])
        y2 = int(second_pair[1])

        is_horizontal = y1 == y2
        is_vertical = x1 == x2
        if is_vertical or is_horizontal:
            mark_segments(x1, y1, x2, y2, board)
        else:
            continue

    for row in board:
        print(row)
