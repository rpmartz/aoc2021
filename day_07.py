def read_file():
    with open('data/day07.txt', 'r') as f:
        return [int(num) for num in f.read().split(',')]

def total_cost(num_steps):
    cost = 0
    cost_for_step = 1
    for i in range(0, num_steps):
        cost = cost + cost_for_step
        cost_for_step += 1

    return cost

def find_best_alignment(positions, cost_fn):
    min_distance = 999999999999999
    best_position = None
    for number in positions:
        distance_for_number = sum(cost_fn(abs(number - point)) for point in positions)

        if distance_for_number < min_distance:
            min_distance = distance_for_number
            best_position = number

    return best_position, min_distance

if __name__ == '__main__':
    starting_positions = read_file()
    best_position, fuel_cost = find_best_alignment(starting_positions, lambda x: x)
    print(fuel_cost)

    best_position, fuel_cost = find_best_alignment(starting_positions, total_cost)
    print(fuel_cost)
