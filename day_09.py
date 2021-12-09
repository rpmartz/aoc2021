def find_low_points(board):
    pass


def calculate_risk_level(low_points):
    return sum(1 + p for p in low_points)
