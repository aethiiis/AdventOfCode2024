from itertools import product

def processing():
    equations = [[int(equation[0]), list(map(int, equation[1].split()))] 
    for equation in (line.split(": ") 
    for line in open("src/day07/input.txt").read().splitlines())]

    return equations

def obtainable(result, numbers, concat):
    if len(numbers) == 1:
        return result == numbers[0]

    if result % numbers[-1] == 0 and obtainable(result // numbers[-1], numbers[:-1], concat):
        return True

    if result > numbers[-1] and obtainable(result - numbers[-1], numbers[:-1], concat):
        return True
    
    if concat:
        r, n = str(result), str(numbers[-1])
        
        if len(r) > len(n) and r.endswith(n) and obtainable(int(r[:-len(n)]), numbers[:-1], concat):
            return True

def part1():
    equations = processing()
    sum = 0

    for equation in equations:
        result = equation[0]
        numbers = equation[1]

        if obtainable(result, numbers, False):
            sum += result
    
    return sum

def part2():
    equations = processing()
    sum = 0

    for equation in equations:
        result = equation[0]
        numbers = equation[1]

        if obtainable(result, numbers, True):
            sum += result
    
    return sum

if __name__ == "__main__":
    print(part1())
    print(part2())