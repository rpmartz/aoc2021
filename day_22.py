def parse_range(range_notation):
    """
    parses a range notation like x=10..12 to a start and stop, (10, 13) in this case
    """

    start_and_stop_with_dots = range_notation.split('=')
    numbers = start_and_stop_with_dots[1].split('..')

    return int(numbers[0]), int(numbers[1])


def cuboid_from_line(line):
    direction, rest = line.split(' ')

    ranges = line.split(',')
    x_start, x_stop = parse_range(ranges[0])
    y_start, y_stop = parse_range(ranges[1])
    z_start, z_stop = parse_range(ranges[0])

    cuboids = set()

    for x in range(x_start, x_stop + 1):
        for y in range(y_start, y_stop + 1):
            for z in range(z_start, z_stop + 1):
                cuboids.add((x, y, z))

    return direction, cuboids


if __name__ == '__main__':
    line = 'on x=10..12,y=10..12,z=10..12'
