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


def mark_horizontal_line(board, row_index, x1, x2):
    for column in range(x1, x2 + 1):
        board[row_index][column] = board[row_index][column] + 1

def mark_vertical_line(board, column_index, y1, y2):
    for row in range(y1, y2 + 1):
        board[row][column_index] = board[row][column_index] + 1

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
        if is_vertical:
            mark_vertical_line(board, x1, y1, y2)
        elif is_horizontal:
            mark_horizontal_line(board, y1, x1, x2)
        else:
            continue

    for row in board:
        print(row)
