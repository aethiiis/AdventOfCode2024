import functools

def processing():
    stones = list(map(int, open("src/day11/input.txt").read().split(" ")))
    return stones

@functools.cache
def handle_stone(stone, times):
    if not times:
        return 1
    elif not stone:
        return handle_stone(1, times-1)
    elif (s := str(stone)) and not (l := len(s)) % 2:
        return handle_stone(int(s[:l//2]), times-1) + handle_stone(int(s[l//2:]), times-1)
    else:
        return handle_stone(stone*2024, times-1)

def part1() -> int:
    stones = processing()
    return sum(handle_stone(stone, 25) for stone in stones)


def part2() -> int:
    stones = processing()
    return sum(handle_stone(stone, 75) for stone in stones)

if __name__ == "__main__":
    print(part1())
    print(part2())