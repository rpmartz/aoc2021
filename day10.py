SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def find_corruption(sequence):
    openers = {'{', '(', '[', '<'}
    closers = {'}', ')', ']', '>'}

    closers_to_openers = {
        '}': '{', ')': '(', '>': '<', ']': '['
    }

    stack = []
    for character in sequence:
        if character in openers:
            stack.append(character)
        elif character in closers:
            last_opener = stack.pop()
            expected_opener = closers_to_openers[character]
            if last_opener != expected_opener:
                return character

    return None


with open('data/day10.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

score = 0
for line in lines:
    first_illegal_character = find_corruption(line)
    if first_illegal_character:
        score += SCORES[first_illegal_character]

print(score)
