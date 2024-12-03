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
    total_distance = 0
    for i in range(len(left)):
        total_distance += abs(left[i] - right[i])

    return total_distance

def part2():
    left, right = processing()

    # Calculate how many times a number is in each list
    l = Counter(left)
    r = Counter(right)
    
    # Calculate the similarity score
    similarity_score = 0
    for key, value in l.items():
        similarity_score += 0 if key not in r else key * value * r[key]
    
    return similarity_score

if __name__ == "__main__":
    print(part1())
    print(part2())