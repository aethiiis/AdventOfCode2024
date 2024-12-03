def processing():
    # Extract raw data
    with open("src/day02/input.txt", "r") as input:
        lines = [[int(num) for num in line.split()] for line in input]
    
    return lines

def part1():
    lines:list[list[int]] = processing()

    # Iterate through the lines to check whether they're safe
    count = 0
    for i in range(len(lines)):
        safe = check_safe(lines[i])

        if safe:
            count += 1
    
    return count

def part2():
    lines:list[list[int]] = processing()

    # Iterate through the lines to check whether they're safe
    count = 0
    for i in range(len(lines)):
        safe = check_safe(lines[i])

        # If initial check failed, check whether any sublist can pass
        if not safe:
            possibilites:list[list[int]] = [lines[i][:j] + lines[i][j+1:] for j in range(len(lines[i]))]
            for j in range(len(possibilites)):
                if check_safe(possibilites[j]):
                    safe = True
                    break

        if safe:
            count += 1

    return count

def check_safe(line:list) -> bool:
    # Checks whether an individual report is safe
    safe = True
    increase = 0
    
    for j in range(len(line) - 1):
        if increase == 0:
            if line[j] > line[j+1] and 1 <= abs(line[j] - line[j+1]) <= 3:
                increase = 1
            elif line[j] < line[j+1] and 1 <= abs(line[j] - line[j+1]) <= 3:
                increase = -1
            else:
                safe = False
                break
        
        elif increase == 1:
            if line[j] < line[j+1] or abs(line[j] - line[j+1]) < 1 or abs(line[j] - line[j+1]) > 3:
                safe = False
                break

        else:
            if line[j] > line[j+1] or abs(line[j] - line[j+1]) < 1 or abs(line[j] - line[j+1]) > 3:
                safe = False
                break
    
    return safe

if __name__ == "__main__":
    print(part1())
    print(part2())