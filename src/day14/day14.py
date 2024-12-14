def processing() -> list:
    input = open("src/day14/input.txt").read().splitlines()
    robots = []
    for line in input:
        pos, vit = line.split(" ")
        pos = tuple(map(int, pos.split("=")[1].split(",")))
        vit = tuple(map(int, vit.split("=")[1].split(",")))

        robots.append([pos, vit])
    
    return robots

def all_distinct(robots) -> bool:
    grid = dict()

    for robot in robots:
        if robot[0] in grid:
            return False
        else:
            grid[robot[0]] = 1
    
    return True

def parcours(robots) -> None:
    width = 101
    height = 103
    for robot in robots:
        x, y = robot[0]
        vx, vy = robot[1]

        robot[0] = ((x+vx)%width, (y+vy)%height)

def part1() -> int:
    robots = processing()
    width = 101
    height = 103
    
    for t in range(100):
        parcours(robots)
    
    top_left = 0
    top_right = 0
    bottom_left = 0
    bottom_right = 0

    for robot in robots:
        if robot[0][0] < width//2 and robot[0][1] < height//2:
            top_left += 1
        
        elif robot[0][0] > width//2 and robot[0][1] < height//2:
            top_right += 1
        
        elif robot[0][0] < width//2 and robot[0][1] > height//2:
            bottom_left += 1
        
        elif robot[0][0] > width//2 and robot[0][1] > height//2:
            bottom_right += 1
    
    return top_left*top_right*bottom_left*bottom_right

def part2() -> int:
    robots = processing()
    t = 0

    while not all_distinct(robots):
        t += 1
        parcours(robots)
    
    return t


if __name__ == "__main__":
    print(part1())
    print(part2())