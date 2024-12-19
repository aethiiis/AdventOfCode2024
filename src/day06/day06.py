def processing() -> dict[complex, str]:
    return {i + j * 1j: c for i, r in enumerate(open("src/day06/input.txt").readlines()) for j, c in
            enumerate(r.strip())}


def loop(grid: dict[complex, str], start: complex) -> tuple[set[complex], bool]:
    p, d, visited = start, -1, set()
    while p in grid and (p, d) not in visited:
        visited.add((p, d))
        if grid.get(p+d) == "#":
            d *= -1j
        else:
            p += d
    return {p for p, _ in visited}, (p, d) in visited


def part1() -> int:
    grid: dict[complex, str] = processing()
    return len(loop(processing(), [p for p in grid if grid[p] == '^'][0])[0])


def part2() -> int:
    grid: dict[complex, str] = processing()
    start: complex = [p for p in grid if grid[p] == '^'][0]
    return sum(loop(grid | {o: '#'}, start)[1] for o in loop(grid, start)[0] if o != start)


if __name__ == "__main__":
    print(part1())
    print(part2())
