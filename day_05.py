def read_file():
    with open('data/day05.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]

def build_board():
    """
    build 1000 x 1000 board of zeros
    """
    board = list()
    for i in range(0, 1000):
        row = []
        for j in range(0, 1000):
            row.append(0)

        board.append(row)

    return board


if __name__ == '__main__':
    lines = read_file()
    board = build_board()
