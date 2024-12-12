from queue import Queue

def processing():
    input = [[char for char in line] for line in open("src/day12/input.txt").read().splitlines()]
    garden = dict()

    rows = len(input)
    cols = len(input[0])

    for r in range(rows):
        for c in range(cols):
            garden[(r, c)] = input[r][c]
    
    return garden, rows, cols

def blow_garden(garden, rows, cols):
    new = dict()
    for r in range(rows):
        for c in range(cols):
            new[(3*r, 3*c)] = garden[(r, c)]
            new[(3*r+1, 3*c)] = garden[(r, c)]
            new[(3*r+2, 3*c)] = garden[(r, c)]
            new[(3*r, 3*c+1)] = garden[(r, c)]
            new[(3*r+1, 3*c+1)] = garden[(r, c)]
            new[(3*r+2, 3*c+1)] = garden[(r, c)]
            new[(3*r, 3*c+2)] = garden[(r, c)]
            new[(3*r+1, 3*c+2)] = garden[(r, c)]
            new[(3*r+2, 3*c+2)] = garden[(r, c)]
    
    return new

def neighbors(r, c, rows, cols, garden, plant):
    valid = []

    # Up
    if r-1 >= 0 and garden[(r-1, c)] == plant:
        valid.append((r-1, c))
    
    # Down
    if r+1 <= rows-1 and garden[(r+1, c)] == plant:
        valid.append((r+1, c))

    # Left
    if c-1 >= 0 and garden[(r, c-1)] == plant:
        valid.append((r, c-1))
    
    # Right
    if c+1 <= cols-1 and garden[(r, c+1)] == plant:
        valid.append((r, c+1))
    
    return valid

def part1() -> int:
    garden, rows, cols = processing()
    sum = 0

    # Exploration des régions
    visited = set()
    for (r, c), plant in garden.items():
        if (r, c) in visited:
            continue

        region = {(r, c)}
        perimeter = 0
        frontier = Queue()
        frontier.put((r, c))

        while not frontier.empty():
            (rr, cc) = frontier.get()
            same = neighbors(rr, cc, rows, cols, garden, plant)

            if len(same) < 4:
                perimeter += 4 - len(same)
            
            for x in same:
                if x not in region:
                    frontier.put(x)
                    region.add(x)

        visited.update(region)
        sum += perimeter*len(region)
    
    return sum

def part2() -> int:
    garden, rows, cols = processing()
    sum = 0
    garden = blow_garden(garden, rows, cols)

    # Exploration des régions
    visited = set()
    for (r, c), plant in garden.items():
        if (r, c) in visited:
            continue

        region = {(r, c)}
        border = []
        frontier = Queue()
        frontier.put((r, c))

        while not frontier.empty():
            (rr, cc) = frontier.get()
            same = neighbors(rr, cc, 3*rows, 3*cols, garden, plant)

            if len(same) < 4:
                border.append((rr, cc))
            
            for x in same:
                if x not in region:
                    frontier.put(x)
                    region.add(x)

        # Comptage des côtés
        border.sort()
        point = border[0]
        direction = (0, 1)
        sides = 1
        while border:
            r, c = point[0], point[1]
            dr, dc = direction[0], direction[1]
            border.remove(point)

            if (r+dr, c+dc) in border:
                point = (r+dr, c+dc)
                continue

            # On regarde :
            # en haut
            if direction != (-dr, -dc) and (r-1, c) in border:
                direction = (-1, 0)
                sides += 1
                point = (r-1, c)
            
            # en bas
            elif direction != (-dr, -dc) and (r+1, c) in border:
                direction = (1, 0)
                sides += 1
                point = (r+1, c)
            
            # à gauche
            elif direction != (-dr, -dc) and (r, c-1) in border:
                direction = (0, -1)
                sides += 1
                point = (r, c-1)
            
            # à droite
            elif direction != (-dr, -dc) and (r, c+1) in border:
                direction = (0, 1)
                sides += 1
                point = (r, c+1)
            
            elif ((r-1, c+dc) in border) and (dc == 1 or dc == -1):
                direction = (-1, 0)
                sides += 1
                point = (r-1, c+dc)

            elif ((r+1, c+dc) in border) and (dc == 1 or dc == -1):
                direction = (1, 0)
                sides += 1
                point = (r+1, c+dc)
            
            elif ((r+dr, c-1) in border) and (dr == 1 or dr == -1):
                direction = (0, -1)
                sides += 1
                point = (r+dr, c-1)
            
            elif ((r+dr, c+1) in border) and (dr == 1 or dr == -1):
                direction = (0, 1)
                sides += 1
                point = (r+dr, c+1)
            
            elif border:
                point = border[0]
                direction = (border[0][0] - border[1][0], border[0][1] - border[1][1])

        visited.update(region)
        sum += int(sides*len(region)/9)
    
    return sum

if __name__ == "__main__":
    print(part1())
    print(part2())