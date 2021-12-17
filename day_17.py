def build_target_grid(x_open, x_close, y_open, y_close):
    grid = set()
    for x in range(x_open, x_close + 1):
        for y in range(y_open, y_close - 1, -1):
            grid.add((x, y))

    return grid


def process_step(x, y):
    if x == 0:
        d_x = 0
    elif x > 0:
        d_x = -1
    else:
        d_x = 1

    new_x = x + d_x
    new_y = y - 1
    return (new_x, new_y)


if __name__ == '__main__':
    target_grid = build_target_grid(150, 171, -70, -129)

    point =
