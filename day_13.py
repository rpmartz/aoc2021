def read_points():
    with open('data/day13-points.txt', 'r') as f:
        return [(int(line.strip().split(',')[0]), int(line.strip().split(',')[1])) for line in f.readlines()]


if __name__ == '__main__':
    lines = read_points()
    for line in lines:
        print(lines)
