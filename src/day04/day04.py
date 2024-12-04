def processing():
    with open("src/day04/input.txt", "r") as input:
        grid = [list(line.strip()) for line in input.readlines()]

    return grid

def part1():

    grid = processing()
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    count = 0
    word = "XMAS"

    rows = len(grid)
    cols = len(grid[0])
    length = len(word)

    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                if all(0 <= row + dr * i < rows and 0 <= col + dc * i < cols and
                       grid[row + dr * i][col + dc * i] == word[i] for i in range(length)):
                    count += 1
    
    return count

def part2():
    grid = processing()
    count = 0

    for row in range (1, len(grid)-1):
        for col in range(1, len(grid[0])-1):
            if grid[row][col] == "A":
                if ((grid[row-1][col-1] == "M" and grid[row+1][col-1] == "S" and grid[row-1][col+1] == "M" and grid[row+1][col+1] == "S") 
                    or (grid[row-1][col-1] == "S" and grid[row+1][col-1] == "M" and grid[row-1][col+1] == "S" and grid[row+1][col+1] == "M") 
                    or (grid[row-1][col-1] == "M" and grid[row+1][col-1] == "M" and grid[row-1][col+1] == "S" and grid[row+1][col+1] == "S") 
                    or (grid[row-1][col-1] == "S" and grid[row+1][col-1] == "S" and grid[row-1][col+1] == "M" and grid[row+1][col+1] == "M")):
                    count += 1
    
    return count

if __name__ == "__main__":
    print(part1())
    print(part2())