def read_file():
    with open('data/day05.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]


if __name__ == '__main__':
    lines = read_file()