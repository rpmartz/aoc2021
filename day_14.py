from collections import Counter

problem_start_template = 'OFSNKKHCBSNKBKFFCVNB'


def read_rules():
    with open('data/day14.txt', 'r') as f:
        return f.read()


def parse_rules(rules: str):
    pair_mappings = {}
    for pairing in rules.splitlines():
        lhs, rhs = pairing.split('->')
        pair_mappings[lhs.strip()] = rhs.strip()

    return pair_mappings


def process(template, rules: dict):
    characters = [c for c in template]
    new_polymer = ''
    for i, _ in enumerate(characters[1:]):
        first = template[i]
        second = template[i + 1]

        pair = first + second
        new_polymer += first
        if pair in rules:
            new_polymer += rules[pair]

        if i == len(characters[1:]) - 1:
            new_polymer += second

    return new_polymer


def quantify(polymer):
    counter = Counter()
    counter.update([c for c in polymer])

    return max(counter.values()) - min(counter.values())


if __name__ == '__main__':
    pass
