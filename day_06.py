

def process_day(fish_list):
    new_fish = []
    for index, days_left in enumerate(fish_list):
        if days_left == 0:
            new_fish.append(8)
            fish_list[index] = 6
        else:
            fish_list[index] = fish_list[index] - 1

    if new_fish:
        fish_list.extend(new_fish)

if __name__ == '__main__':
    with open('data/day06.txt', 'r') as f:
        starting_state = f.read()
        fish = [int(val) for val in starting_state.split(',')]

    for x in range(0, 256):
        process_day(fish)

    print(len(fish))




# model each fish as a single number that represents the number of days until it creates a new lanternfish.


