from itertools import product

def processing():
    grid = [list(line) for line in open("src/day08/input.txt").read().splitlines()]
    return grid

def calculate_antinodes(node1, node2):
    return (node1[0] - (node2[0] - node1[0]), node1[1] - (node2[1] - node1[1])), (node2[0] + (node2[0] - node1[0]), node2[1] + (node2[1] - node1[1]))

def calculate_resonance(node1, node2, grid):
    x1, y1 = node1
    x2, y2 = node2

    dx = x2 - x1
    dy = y2 - y1

    rows = len(grid)
    cols = len(grid[0])

    max_dx = rows // dx
    max_dy = cols // dy

    nodes = list()

    for i in range(max(max_dx, max_dy)):
        nodes.append((x1-i*dx, y1-i*dy))
        nodes.append((x2+i*dx, y2+i*dy))
    
    return nodes

def find_frequencies(grid):
    nodes = dict()
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            node = grid[r][c]

            if node != ".":
                if node not in nodes:
                    nodes[node] = [(r, c)]
                
                else:
                    nodes[node].append((r, c))
    
    return nodes


def is_in(node, grid):
    return (0 <= node[0] <= len(grid)-1 and 0 <= node[1] <= len(grid)-1)

def part1():
    grid = processing()
    antinodes = set()
    nodes = find_frequencies(grid)

    for antennas in nodes.values():
        pairs = [[x, y] for x, y in product(antennas, repeat=2) if x != y]

        for pair in pairs:
            node1, node2 = pair
            antinode1, antinode2 = calculate_antinodes(node1, node2)
            
            if is_in(antinode1, grid):
                antinodes.add(antinode1)
            
            if is_in(antinode2, grid):
                antinodes.add(antinode2)
    
    return len(antinodes)

def part2():
    grid = processing()
    antinodes = set()
    nodes = find_frequencies(grid)

    for antennas in nodes.values():
        pairs = [[x, y] for x, y in product(antennas, repeat=2) if x != y]

        for pair in pairs:
            node1, node2 = pair
            potential_antinodes = calculate_resonance(node1, node2, grid)
            
            for antinode in potential_antinodes:
                if is_in(antinode, grid):
                    antinodes.add(antinode)
    
    return len(antinodes)

if __name__ == "__main__":
    print(part1())
    print(part2())