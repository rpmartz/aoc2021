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

    corners = {(150, -70), (150, -129), (171, -129), (171, -129)}
    if not all([point in target_grid for point in corners]):
        print('Check bounds')

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
