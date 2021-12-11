def count_num_flashes(board, iteration):
    for step in range(iteration):

        flashed_this_step = set()

        for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element < 9:
                    board[i][j] = board[i][j] + 1
                # if element has flashed, increment neighbors by one
                elif element == 9:
                    process_flash(board, i, j, flashed_this_step)
                    board[i][j] = 0


def process_flash(board, i, j, already_flashed):
    neighbors = get_neighbors(board, i, j)
    for neighbor in neighbors:
        x, y = neighbor
        if board[x][y] < 9 and neighbor not in already_flashed:
            board[x][y] = board[x][y] + 1
        elif board[x][y] == 9 and neighbor not in already_flashed:
            already_flashed.add(neighbor)
            board[x][y] = 0
            process_flash(board, x, y, already_flashed)
        else:
            raise Exception('Should not reach this point during recursion')


def get_neighbors(board, i, j):
    height = len(board)
    width = len(board[0])

    neighbors = set()
    # left
    if j > 0:
        neighbors.add((i, j - 1))
    # right
    if j + 1 < width:
        neighbors.add((i, j + 1))
    # top
    if i > 0:
        neighbors.add((i - 1, j))
    # bottom
    if i + 1 < height:
        neighbors.add((i + 1, j))
    # diagonal upper left
    if i > 0 and j > 0:
        neighbors.add((i - 1, j - 1))

    # diagonal upper right
    if i > 0 and j + 1 < width:
        neighbors.add((i - 1, j + 1))

    # diagonal lower left
    if i + 1 < height and j > 0:
        neighbors.add((i + 1, j - 1))
    # diagonal lower right
    if i + 1 < height and j + 1 < width:
        neighbors.add((i + 1, j + 1))

    return set(neighbors)
