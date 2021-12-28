from aocutils import read_numeric_grid, get_neighbors, Point


def read_file():
    with open('data/day15.txt', 'r') as f:
        return f.read()


def calculate_min_risk(grid) -> int:
    start = Point(0, 0)

    queue = [start]
    while queue:
        position = queue.pop(0)
        neighbors = get_neighbors(position, 8)

        for neighbor in neighbors:
            if neighbor not in grid:
                # some neighbors will be off of the board/grid
                continue

            if grid[neighbor] != 'reached':
                grid[neighbor] = 'reached'
                queue.append(neighbor)

    return -2


if __name__ == '__main__':
    grid = read_numeric_grid(read_file())
    print(grid)
