def read_points():
    with open('data/day13-points.txt', 'r') as f:
        return [(int(line.strip().split(',')[0]), int(line.strip().split(',')[1])) for line in f.readlines()]


def read_folds():
    with open('data/day13-folds.txt', 'r') as f:
        return [(line.split('=')[0], int(line.split('=')[1])) for line in f.readlines()]


if __name__ == '__main__':
    lines = read_points()
    folds = read_folds()
    for fold in folds:
        print(fold)
