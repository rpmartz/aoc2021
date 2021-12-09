with open('data/day08.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def do_part_one(lines):
    unique_segment_lengths = {2, 3, 4, 7}

    digit_count = 0

    for line in lines:
        output_values = line.split('|')[1]

        for code in output_values.split():
            if len(code) in unique_segment_lengths:
                digit_count += 1

    print(digit_count)

def do_part_two(lines):
    for line in lines:
        lhs, rhs = line.split('|')


do_part_one(lines)
do_part_two(lines)