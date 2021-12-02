
def read_file():
    with open('data/day02.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]

def part_one(lines):
    x = 0
    y = 0
    for line in lines:
        components = line.split(' ')
        direction = components[0]
        magnitude = int(components[1])

        if direction == 'forward':
            x = x + magnitude
        elif direction == 'up':
            y = y - magnitude
        elif direction == 'down':
            y = y + magnitude

    print('End position is %s, %s' % (x, y))
    print('Product of end position is %d' % (x * y))

if __name__ == '__main__':
    lines = read_file()
    part_one(lines)
