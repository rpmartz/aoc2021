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


def calculate_min_risk(grid) -> int:
    start = Point(0, 0)
    goal = Point(99, 99)

    # use a priority queue
    queue = PriorityQueue()
    queue.put(start, 0)

    came_from = {start: None}

    # add way to keep track of movement cost
    cost_so_far = {start: 0}

    while not queue.empty():
        position = queue.get()
        neighbors = get_neighbors(position, 8)

        # early exit once we have explored enough to get to the end
        if position == goal:
            break

        for neighbor in neighbors:
            if neighbor not in grid:
                # some neighbors will be off of the board/grid
                continue

            # cost to neighbor (risk score in this problem's context) is the cost to get to the position
            # plus the cost of the new node
            new_cost = cost_so_far[position] + grid[neighbor]
            if neighbor not in cost_so_far or new_cost < cost_so_far[position]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost
                queue.put(neighbor, priority)

                came_from[neighbor] = position

    # now we can reconstruct a path back to the front
    path = []

    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()
    print(path)

    return -2


if __name__ == '__main__':
    grid = read_numeric_grid(read_file())
    calculate_min_risk(grid)
