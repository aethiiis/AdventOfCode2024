from queue import PriorityQueue

def processing():
    input = open("src/day16/input.txt").read().splitlines()
    grid = {(r, c): v for r in range(len(input)) for c, v in enumerate(input[r])}
    return grid, len(input), len(input[0])

def dijkstra(grid, starts, rows, cols):
    frontier = PriorityQueue()
    best = dict()
    for start in starts:
        node, direction = start
        frontier.put((0, node, direction))

    while not frontier.empty():
        cost, node, direction = frontier.get()

        if (node, direction) in best and cost >= best[(node, direction)]:
            continue

        best[(node, direction)] = cost

        for dr, dc in [direction, (direction[1], -direction[0]), (-direction[1], direction[0])]:
            r, c = node[0] + dr, node[1] + dc

            if 0 <= r < rows and 0 <= c < cols and grid[(r, c)] in ['.', 'S', 'E'] and (dr, dc) == direction:
                frontier.put((cost + 1, (r, c), (dr, dc)))

            if (dr, dc) != direction:
                frontier.put((cost + 1000, node, (dr, dc)))
    
    return best

def part1() -> int:
    grid, rows, cols = processing()

    start = (rows-2, 1)
    end = (1, cols-2)

    paths = dijkstra(grid, [[start, (0, 1)]], rows, cols)
    best = float('inf')
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if (end, (dr, dc)) in paths:
            best = min(best, paths[(end, (dr, dc))])

    return best

def part2() -> int:
    grid, rows, cols = processing()

    start = (rows-2, 1)
    end = (1, cols-2)

    from_start = dijkstra(grid, [[start, (0, 1)]], rows, cols)
    from_end = dijkstra(grid, [[end, (dr, dc)] for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]], rows, cols)

    best = float('inf')
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if (end, (dr, dc)) in from_start:
            best = min(best, from_start[(end, (dr, dc))])
    
    track = set()
    for r in range(rows):
        for c in range(cols):
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                key1 = ((r, c), (dr, dc))
                key2 = ((r, c), (-dr, -dc))
                if key1 in from_start and key2 in from_end and from_start[key1] + from_end[key2] == best:
                    track.add((r, c))
    
    return len(track)

if __name__ == "__main__":
    print(part1())
    print(part2())