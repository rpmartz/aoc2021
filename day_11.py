def count_num_flashes(board, iteration):
    print('counting number of flashes for board after %s' % iteration)
    total_flashes = 0
    for step in range(iteration):

        flashed_this_step = set()

        for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element < 9:
                    board[i][j] = board[i][j] + 1
                # if element has flashed, increment neighbors by one
                else:
                    process_flash(board, i, j, flashed_this_step)
                    board[i][j] = 0
        total_flashes += len(flashed_this_step)
        print('\tAfter adding %s flashes from step %s, total flashes: %s' % (
            len(flashed_this_step), step + 1, total_flashes))

    return total_flashes


def process_flash(board, i, j, already_flashed):
    neighbors = get_neighbors(board, i, j)
    print('\t\tFound %s neighbors of (%s, %s)' % (len(neighbors), i, j))
    for neighbor in neighbors:
        x, y = neighbor
        if board[x][y] < 9 and neighbor not in already_flashed:
            print('\t\t\tPost-flash normal increment for (%s, %s). Old val: %s' % (x, y, board[x][y]))
            board[x][y] = board[x][y] + 1
        elif board[x][y] == 9 and neighbor not in already_flashed:
            print('\t\t\tFlash as result of another flash for (%s, %s). Old val: %s' % (x, y, board[x][y]))
            already_flashed.add(neighbor)
            board[x][y] = 0
            process_flash(board, x, y, already_flashed)


def get_neighbors(i, j):
    neighbors = set()

    for x_offset in (-1, 0, 1):
        for y_offset in (-1, 0, 1):
            if x_offset == 0 and y_offset == 0:
                continue
            neighbors.add((i + x_offset, j + y_offset))

    return neighbors
