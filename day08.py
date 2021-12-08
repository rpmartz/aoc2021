with open('data/day08.txt') as f:
    lines = [line.strip() for line in f.readlines()]

unique_segment_lengths = {2, 3, 4, 7}

digit_count = 0

for line in lines:
    output_values = line.split('|')[1]

    for code in output_values.split():
        if len(code) in unique_segment_lengths:
            digit_count += 1

print(digit_count)
