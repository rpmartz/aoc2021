from aocutils import read_numeric_grid


def read_file():
    with open('data/day15.txt', 'r') as f:
        return f.read()


if __name__ == '__main__':
    grid = read_numeric_grid(read_file())
    print(grid)
