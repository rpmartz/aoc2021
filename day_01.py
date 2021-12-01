def read_file():
    with open('data/day01.txt', 'r') as f:
        return [int(line.strip()) for line in f.readlines()]


def do_part_one():
    lines = read_file()
    num_increases = 0

    for idx, current_measurement in enumerate(lines):
        previous_measurement = lines[idx - 1]
        if current_measurement > previous_measurement:
            num_increases += 1

    print('Number of times sonar depth reading increased: %d' % num_increases)


def do_part_two():
    lines = read_file()
    previous_sum = 1234567899887  # arbitraily large first value
    num_increases = 0

    for idx in range(0, len(lines) - 2):
        a = lines[idx]
        b = lines[idx + 1]
        c = lines[idx + 2]

        current_sum = a + b + c
        if current_sum > previous_sum:
            num_increases += 1

        previous_sum = current_sum

    print('%d sliding windows have increasing sums' % num_increases)


if __name__ == '__main__':
    do_part_one()
    do_part_two()
