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


def find_max_height_for_initial_velocity(dx, dy, grid_x0, grid_x1, grid_y0, grid_y1):
    position = 0, 0
    max_height = 0
    while True:
        # update position based on vector
        position = position[0] + dx, position[1] + dy
        max_height = max(max_height, position[1])

        # check whether we have hit target and add max and exit if so
        within_x_bounds = grid_x0 <= position[0] <= grid_x1
        within_y_bounds = grid_y0 <= position[1] <= grid_y1
        if within_x_bounds and within_y_bounds:
            return max_height

        # check whether we are outside bounds of grid and exit if so
        missed_horizontally = (dx == 0 and position[0] < grid_x0) or (dx == 0 and position[0] > grid_x1)
        missed_vertically = position[1] < grid_y1
        if missed_horizontally or missed_vertically:
            return None

        # update velocity based on steps

        dx, dy = process_step(dx, dy)


if __name__ == '__main__':
    target_grid = build_target_grid(150, 171, -70, -129)

    initial_position = (0, 0)
    max_y = -999999999
    for d_x in range(172, 0, -1):
        for d_y in range(-130, 500):

            # d_x, d_y is vector of initial launch
            # run steps
            position = (0 + d_x, 0 + d_y)
            # iterate until either probe in target or we know probe missed
            heights = set()
            while True:
                heights.add(position[1])
                position = process_step(position[0], position[1])

                if position in target_grid:
                    # capture max height and end iteration
                    max_y = max(max_y, max(heights))
                    break
                elif position[0] > 171 or position[1] < -129:
                    break

    print(max_y)
