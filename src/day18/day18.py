from queue import PriorityQueue


def processing():
    bits = [tuple(map(int, bit.split(","))) for bit in open("src/day18/input.txt").read().splitlines()]
    rows = 71
    cols = 71
    grid = [["." for _ in range(cols)] for _ in range(rows)]
    return grid, bits, rows, cols


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])

    frontier = PriorityQueue()
    frontier.put((0, start))

    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        cost, node = frontier.get()

        if node == end:
            break

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            r, c = node[0] + dr, node[1] + dc
            new_cost = cost + 1

            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "." and (
                    (r, c) not in cost_so_far or new_cost < cost_so_far[(r, c)]):
                frontier.put((new_cost + heuristic(end, (r, c)), (r, c)))
                came_from[(r, c)] = node
                cost_so_far[(r, c)] = new_cost

    current = end
    path = []

    if end not in came_from:
        return []

    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()

    return path


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n


def part1() -> str:
    grid, bits, rows, cols = processing()
    start = (0, 0)
    end = (rows - 1, cols - 1)

    for (r, c) in bits[:1024]:
        grid[r][c] = "#"

    frontier = PriorityQueue()
    frontier.put((0, start))
    best = dict()

    while not frontier.empty():
        cost, (r, c) = frontier.get()

        if (r, c) == end:
            return cost

        if (r, c) in best and cost >= best[(r, c)]:
            continue

        best[(r, c)] = cost

        for nr, nc in [(r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)]:
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == ".":
                frontier.put((cost + 1, (nr, nc)))


def part2() -> str:
    grid, bits, rows, cols = processing()
    start = (0, 0)
    end = (rows - 1, cols - 1)
    path = astar(grid, start, end)

    for i in range(len(bits)):
        r, c = bits[i]
        grid[r][c] = "#"

        if (r, c) in path:
            path = astar(grid, start, end)

            if len(path) == 0:
                return ",".join(map(str, (r, c)))


if __name__ == "__main__":
    print(part1())
    print(part2())
