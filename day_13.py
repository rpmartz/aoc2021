def read_points():
    with open('data/day13-points.txt', 'r') as f:
        return [(int(line.strip().split(',')[0]), int(line.strip().split(',')[1])) for line in f.readlines()]


def read_folds():
    with open('data/day13-folds.txt', 'r') as f:
        return [(line.split('=')[0], int(line.split('=')[1])) for line in f.readlines()]


def process_fold(points, fold):
    points_after_fold = set()

    axis, value = fold
    for idx, point in enumerate(points):
        p_x, p_y = point
        if axis == 'x':
            # fold right half left
            if p_x > value:
                # x value of point shifts twice distance from p_x to value
                distance = value - p_x
                new_point = (-2 * distance, p_y)
                points_after_fold.add(new_point)
            else:
                points_after_fold.add(point)

        elif axis == 'y':
            # fold bottom half up
            if p_y > value:
                distance = value - p_y
                new_point = (p_x, -2 * distance)
                points_after_fold.add(new_point)
            else:
                points_after_fold.add(point)
        else:
            raise Exception('Do not know how to handle %s' % fold)

    return points_after_fold


if __name__ == '__main__':
    points = read_points()
    folds = read_folds()

    first_fold = folds[0]
    points = process_fold(points, first_fold)
    print(len(points))
