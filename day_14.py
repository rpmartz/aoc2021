from collections import Counter

problem_start_template = 'OFSNKKHCBSNKBKFFCVNB'


def read_rules():
    with open('data/day14.txt', 'r') as f:
        return f.read()


def process(template, rules):
    pass


def quantify(polymer):
    counter = Counter()
    counter.update([c for c in polymer])

    return max(counter.values()) - min(counter.values())


if __name__ == '__main__':
    pass
