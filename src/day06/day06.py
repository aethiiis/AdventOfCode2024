def processing():
    map = [list(line) for line in open("src/day06/input.txt").read().split()]

    return map

def find_start(map):
    start_position = (0, 0)
    start_direction = (0, 0)

    rows = len(map)
    cols = len(map[0])

    for r in range(rows):
        for c in range(cols):
            if map[r][c] == '^':
                start_position = (r, c)
                start_direction = (-1, 0)
            elif map[r][c] == '<':
                start_position = (r, c)
                start_direction = (0, -1)
            elif map[r][c] == '>':
                start_position = (r, c)
                start_direction = (0, 1)
            elif map[r][c] == 'v':
                start_position = (r, c)
                start_direction = (1, 0)
    
    return start_position, start_direction

def find_loop(map, start_position, start_direction):
    position = start_position
    direction = start_direction

    visited = set()

    rows = len(map)
    cols = len(map[0])

    while True:
        visited.add(position + direction)

        next_position = tuple(a + b for a, b in zip(position, direction))
        next_r = next_position[0]
        next_c = next_position[1]

        if next_r < 0 or next_r > rows - 1 or next_c < 0 or next_c > cols - 1:
            return False
        
        elif map[next_r][next_c] == "#":
            direction = (direction[1], -direction[0])
        
        else:
            position = next_position
        
        if position + direction in visited:
            return True


def find_exit(map, start_position, start_direction):
    position = start_position
    direction = start_direction
    visited = {position}

    rows = len(map)
    cols = len(map[0])

    while True:
        next_position = tuple(a + b for a, b in zip(position, direction))
        next_r = next_position[0]
        next_c = next_position[1]

        if next_r < 0 or next_r > rows - 1 or next_c < 0 or next_c > cols - 1:
            break

        elif map[next_r][next_c] == "#":
            direction = (direction[1], -direction[0])
        
        else:
            position = next_position
            visited.add(position)
    
    return visited

def part1():
    map = processing()
    position, direction = find_start(map)
    return len(find_exit(map, position, direction))


def part2():
    map = processing()
    position, direction = find_start(map)
    visited = find_exit(map, position, direction)

    count = 0

    for obstacle in visited:
        map[obstacle[0]][obstacle[1]] = "#"

        if find_loop(map, position, direction):
            count += 1
        
        map[obstacle[0]][obstacle[1]] = "."
    
    return count

if __name__ == "__main__":
    print(part1())
    print(part2())