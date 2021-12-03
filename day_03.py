
def read_file():
    with open('data/day03.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]

def part_one(lines):
    positions_to_bit_counts = {
        0: {'0': 0, '1': 0},
        1: {'0': 0, '1': 0},
        2: {'0': 0, '1': 0},
        3: {'0': 0, '1': 0},
        4: {'0': 0, '1': 0},
        5: {'0': 0, '1': 0},
        6: {'0': 0, '1': 0},
        7: {'0': 0, '1': 0},
        8: {'0': 0, '1': 0},
        9: {'0': 0, '1': 0},
        10: {'0': 0, '1': 0},
        11: {'0': 0, '1': 0}
    }

    lines = read_file()
    for line in lines:
        for index, bit in enumerate(line):
            bit_count_for_index = positions_to_bit_counts[index]

            count_for_bit_at_index = bit_count_for_index[bit]
            count_for_bit_at_index += 1
            bit_count_for_index[bit] = count_for_bit_at_index

    result = []
    for bit_count in positions_to_bit_counts.values():
        if bit_count['0'] > bit_count['1']:
            result.append('0')
        else:
            result.append('1')

    gamma = int(''.join(result), 2)
    inverse = int('111111111111', 2)
    epsilon = gamma ^ inverse

    print('gamma: %d' % (gamma))
    print('epsilon: %d' % (epsilon))
    print('gamma * epsilon = %d' % (gamma * epsilon))


if __name__ == '__main__':
    lines = read_file()
    part_one(lines)

    print('\n=== part two ===\n')