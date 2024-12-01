from collections import Counter

def processing():
    # Extract raw data
    with open('src/day01/input.txt', 'r') as input:
        lines = [[int(num) for num in line.split()] for line in input]

    # Transform into two lists
    left = [lines[i][0] for i in range(len(lines))]
    right = [lines[i][1] for i in range(len(lines))]

    return left, right

def part1():
    left, right = processing()

    # Sort the lists
    left.sort()
    right.sort()

    # Calculate the total distance
    sum = 0
    for i in range(len(left)):
        sum += abs(left[i] - right[i])

    return sum

def part2():
    left, right = processing()

    # Calculate how many times a number is in each list
    l = Counter(left)
    r = Counter(right)
    
    # Calculate the similarity score
    sum = 0
    for key, value in l.items():
        sum += 0 if key not in r else key * value * r[key]
    
    return sum

if __name__ == "__main__":
    print(part1())
    print(part2())