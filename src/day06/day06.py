import os
from concurrent.futures import ProcessPoolExecutor

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
    rows, cols = len(map), len(map[0])

    while True:
        current = (position, direction)
        if current in visited:
            return True
        visited.add(current)
        
        visited.add(position + direction)
        next_r, next_c = position[0]+direction[0], position[1]+direction[1]

        if next_r < 0 or next_r > rows - 1 or next_c < 0 or next_c > cols - 1:
            return False
        
        elif map[next_r][next_c] == "#":
            direction = (direction[1], -direction[0])
        
        else:
            position = (next_r, next_c)
        


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

def process_chunk(chunk, map, position, direction):
    count = 0

    for obstacle in chunk:
        map[obstacle[0]][obstacle[1]] = "#"

        if find_loop(map, position, direction):
            count += 1
        
        map[obstacle[0]][obstacle[1]] = "."
    
    return count

def part1():
    map = processing()
    position, direction = find_start(map)
    return len(find_exit(map, position, direction))


def part2():
    grid = processing()
    position, direction = find_start(grid)
    visited = find_exit(grid, position, direction)
    
    # Split the set into 12 chunks
    visited_list = list(visited)
    num_chunks = os.cpu_count()
    chunk_size = len(visited_list) // num_chunks
    chunks = [visited_list[i:i+chunk_size] for i in range(0, len(visited_list), chunk_size)]

    # Multiprocessing
    with ProcessPoolExecutor(max_workers=num_chunks) as executor:
        results = executor.map(process_chunk, chunks, [grid]*num_chunks, [position]*num_chunks, [direction]*num_chunks)

    # Combine
    return sum(results)+1

if __name__ == "__main__":
    print(part1())
    print(part2())