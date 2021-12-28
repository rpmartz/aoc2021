import heapq

from aocutils import read_numeric_grid, get_neighbors, Point


class PriorityQueue:

    def __init__(self):
        self.elements = []

    def empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def read_file():
    with open('data/day15.txt', 'r') as f:
        return f.read()


# TODO this makes for a longer and suboptimal path. Why?
def heuristic(a, b):
    # simple distance between points heuristic
    (x1, y1) = a
    (x2, y2) = b

    return abs(x1 - x2) + abs(y1 - y2)


def h2(a, b):
    return sum(a) - sum(b)


def calculate_min_risk(grid, goal) -> int:
    start = Point(0, 0)

    # use a priority queue
    queue = PriorityQueue()
    queue.put(start, 0)

    came_from = {start: None}

    # add way to keep track of movement cost
    cost_so_far = {start: 0}

    while not queue.empty():
        position = queue.get()

        # early exit once we have explored enough to get to the end
        if position == goal:
            break

        neighbors = get_neighbors(position, 4)

        for neighbor in neighbors:
            if neighbor not in grid:
                # some neighbors will be off of the board/grid
                continue

            # cost to neighbor (risk score in this problem's context) is the cost to get to the position
            # plus the cost of the new node
            new_cost = cost_so_far[position] + grid[neighbor]

            # if we don't yet have a cost to get to this location, or this is a better path, let's process it
            if neighbor not in cost_so_far or new_cost < cost_so_far[position]:
                cost_so_far[neighbor] = new_cost

                # use heuristic function to add distance to the goal to the priority in
                # order to prioritize movement toward goal in search
                priority = new_cost + h2(neighbor, goal)
                queue.put(neighbor, priority)

                came_from[neighbor] = position

    # now we can reconstruct a path back to the start
    path = []

    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]

    return sum(grid[point] for point in path)


if __name__ == '__main__':
    grid = read_numeric_grid(read_file())
    risk_score = calculate_min_risk(grid, Point(99, 99))
    print(risk_score)

    goal = Point(99, 99)
    for point in grid:
        if heuristic(point, goal) != h2(point, goal):
            print(f'Found different heuristic values for {point}')
            print(f'h2: {h2(point, goal)}')
            print(f'heuristic: {heuristic(point, goal)}')
