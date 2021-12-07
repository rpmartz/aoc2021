

def find_best_alignment(positions):
    min_distance = 999999999999999
    best_position = None
    for number in positions:
        distance_for_number = sum(abs(number - point) for point in positions)

        if distance_for_number < min_distance:
            min_distance = distance_for_number
            best_position = number

    return best_position, min_distance



