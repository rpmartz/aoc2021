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

# If you model each number as a 7 bit base 2 number where a is index 0 and f is index 7

# 0 - 1110111
# 1 - 0010010
# 2 - 1011101
# 3 - 1011010
# 4 - 0111010
# 5 - 1101010
# 6 - 1101111
# 7 - 1010010
# 8 - 1111111
# 9 - 1111011

# then you can look at the unique numbers:
# 1 - 0010010
# 4 - 0111010
# 7 - 1010010
# 8 - 1111111

# and given the example:
# 1 - 0010010 ab
# 4 - 0111010 eafb
# 7 - 1010010 dab
# 8 - 1111111 acedgfb