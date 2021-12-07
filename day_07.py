def read_file():
    with open('data/day07.txt', 'r') as f:
        return [int(num) for num in f.read().split(',')]

def find_best_alignment(positions):
    min_distance = 999999999999999
    best_position = None
    for number in positions:
        distance_for_number = sum(abs(number - point) for point in positions)

        if distance_for_number < min_distance:
            min_distance = distance_for_number
            best_position = number

    return best_position, min_distance

if __name__ == '__main__':
    starting_positions = read_file()
    best_position, fuel_cost = find_best_alignment(starting_positions)
    print(fuel_cost)

