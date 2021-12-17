from collections import namedtuple

Point = namedtuple('Point', 'x y')


def get_neighbors(point: Point, num=4) -> set[Point]:
    if num not in {4, 8}:
        raise Exception(f'Invalid argument {num}. Can get 4 or 8 neighbors')

    if num == 4:
        return {Point(x=point.x + 1, y=point.y), Point(x=point.x - 1, y=point.y), Point(x=point.x, y=point.y + 1),
                Point(x=point.x, y=point.y - 1)}
    else:
        neighbors = set()
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x == 0 and y == 0:
                    continue

                neighbors.add(Point(point.x + x, point.y + y))

        return neighbors
