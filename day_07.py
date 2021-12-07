import math


def find_best_alignment(positions):
    min_distance = 999999999999999
    for number in positions:
        distance_for_number = 0
        for point in positions:
            distance_for_number += abs(number - point)

        min_distance = min(min_distance, distance_for_number)

    return min_distance



