def read_file():
    with open('data/day04.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


def build_boards(lines):
    boards = []
    current_board = []
    for line in lines[2:]:
        if not line:
            boards.append(current_board)
            current_board = []

        row = [(int(num), False) for num in line.split(' ') if num != '']
        if row:
            current_board.append(row)

    return boards


def mark_number_seen(number, boards):
    for board in boards:
        for row in board:
            for index, box in enumerate(row):
                if box[0] == number:
                    row[index] = (number, True)


def has_row_bingo(board):
    for row in board:
        if row[0][1] and row[1][1] and row[2][1] and row[3][1] and row[4][1]:
            return True

    return False


def has_column_bingo(board):
    for column in range(0, 5):
        if board[0][column][1] and board[1][column][1] and board[2][column][1] and board[3][column][1] and \
                board[4][column][1]:
            return True

    return False


def has_bingo(board):
    return has_row_bingo(board) or has_column_bingo(board)

def sum_seen_numbers(board):
    return sum([
        item[0] for row in board for item in row if item[1]
    ])

lines = read_file()
bingo_input = [int(num.strip()) for num in lines[0].split(',')]

boards = build_boards(lines)

bingo_seen = False
for number in bingo_input:
    mark_number_seen(number, boards)

    for board in boards:
        if has_bingo(board):
            print('Bingo for board on number %s' % number)
            unseen_num_sum = sum([
                item[0] for row in board for item in row if item[1] == False
            ])

            print('Sum of unseen numbers on winning board: %s' % unseen_num_sum)
            print(unseen_num_sum * number)
            for row in board:
                print(row)
            bingo_seen = True
            break


    if bingo_seen:
        break