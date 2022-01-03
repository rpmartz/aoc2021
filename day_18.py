if __name__ == '__main__':
    with open('data/day18.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        print(line.strip())


def calculate_magnitude(snailfish_number):
    pass

# need to implement addition for snailfish numbers

# [1, 2] + [[3,4], 5] = [[1,2],[[3,4],5]]

# to reduce a snailfish number, you must repeatedly do first action in list that applies:
##  - if any pair nested inside 4 pairs, leftmost pair explodes
##  - if any number is 10 or greater, leftmost regular number splits
