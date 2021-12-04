
def read_file():
    with open('data/day04.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


lines = read_file()
bingo_input = lines[0]

boards = []
current_board = []
for line in lines[2:]:
    if not line:
        boards.append(current_board)
        current_board = []

    current_board.append([(int(num), False) for num in line.split(' ') if num != ''])



