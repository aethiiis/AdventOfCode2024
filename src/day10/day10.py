from queue import Queue

def processing():
    input = [[int(x) for x in line] for line in open("src/day10/input.txt").read().split()]

    rows = len(input)
    cols = len(input[0])

    topo = dict()

    for r in range(rows):
        for c in range(cols):
            topo[(r, c)] = input[r][c]

    return topo, rows, cols

def search(topo, rows, cols, zeroes, memory = True):
    trailheads = dict()

    for zero in zeroes:
        frontier = Queue()
        frontier.put(zero)
        if memory:
            nines = set()

        while not frontier.empty():
            (r, c) = frontier.get()
            value = topo[(r, c)]

            # Top reached
            if value == 9:
                if memory and (r, c) not in nines:
                    nines.add((r, c))
                    if zero not in trailheads:
                        trailheads[zero] = 1

                    else:
                        trailheads[zero] += 1
                
                elif memory:
                    continue
                
                else:
                    if zero not in trailheads:
                        trailheads[zero] = 1
                    else:
                        trailheads[zero] += 1
    
            else:
                valid = neighbors(r, c, rows, cols, topo, value)
                for x in valid:
                    frontier.put(x)
    
    return trailheads

def neighbors(r, c, rows, cols, topo, value):
    valid = []

    # Up
    if r-1 >= 0 and topo[(r-1, c)] == value + 1:
        valid.append((r-1, c))
    
    # Down
    if r+1 <= rows-1 and topo[(r+1, c)] == value + 1:
        valid.append((r+1, c))

    # Left
    if c-1 >= 0 and topo[(r, c-1)] == value + 1:
        valid.append((r, c-1))
    
    # Right
    if c+1 <= cols-1 and topo[(r, c+1)] == value + 1:
        valid.append((r, c+1))
    
    return valid

def part1() -> int:
    topo, rows, cols = processing()
    zeroes = [(r, c) for (r, c), x in topo.items() if x == 0]
    trailheads = search(topo, rows, cols, zeroes)
    
    return sum(x for x in trailheads.values())

def part2() -> int:
    topo, rows, cols = processing()
    zeroes = [(r, c) for (r, c), x in topo.items() if x == 0]
    trailheads = search(topo, rows, cols, zeroes, False)
    
    return sum(x for x in trailheads.values())

if __name__ == "__main__":
    print(part1())
    print(part2())