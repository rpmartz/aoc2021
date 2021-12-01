

def read_file():
    with open('data/day01.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]



def do_part_one():

    lines = read_file()
    num_increases = 0

    for idx, current_measurement in enumerate(lines):
        previous_measurement = lines[idx - 1]
        if current_measurement > previous_measurement:
            num_increases += 1


    print('Number of times sonar depth reading increased: %d' % num_increases)


if __name__ == '__main__':
    do_part_one()
