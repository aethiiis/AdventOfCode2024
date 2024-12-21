def processing() -> list:
    return [list(map(lambda slist: tuple(map(int, slist)), map(lambda x: x.split("=")[1].split(","), line.split(" "))))
            for line in open("src/day14/input.txt").read().splitlines()]


def all_distinct(robots) -> bool:
    grid = dict()

    for robot in robots:
        if robot[0] in grid:
            return False
        else:
            grid[robot[0]] = 1

    return True


def run(robots, t, w=101, h=103) -> int:
    a = b = c = d = 0
    for (x, y), (vx, vy) in robots:
        x, y = (x + vx * t) % w, (y + vy * t) % h
        a += x > w // 2 and y > h // 2
        b += x > w // 2 and y < h // 2
        c += x < w // 2 and y > h // 2
        d += x < w // 2 and y < h // 2
    return a * b * c * d


def part1() -> int:
    return run(processing(), 100)


def part2() -> int:
    return min(range(7038), key=lambda x: run(processing(), x))


if __name__ == "__main__":
    print(part1())
    print(part2())
