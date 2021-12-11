def count_num_flashes(board, iteration):
    for step in range(iteration):
        for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element < 9:
                    board[i][j] = board[i][j] + 1
                # if element has flashed, increment neighbors by one
                elif element == 9:
                    # do flash
                    board[i][j] = 0
