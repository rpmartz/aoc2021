def build_target_grid(x_open, x_close, y_open, y_close):
    grid = set()
    for x in range(x_open, x_close + 1):
        for y in range(y_open, y_close - 1, -1):
            grid.add((x, y))

    return grid


if __name__ == '__main__':
    target_grid = build_target_grid(150, 171, -70, -129)

    if (150, -70) not in target_grid:
        print('expected 150, -70')
    elif (171, -129) not in target_grid:
        print('expected 171, -129')
    elif (160, -100) not in target_grid:
        print('expected 160, -100')
