from itertools import product

def processing():
    equations = [[int(equation[0]), list(map(int, equation[1].split()))] 
    for equation in (line.split(": ") 
    for line in open("src/day07/input.txt").read().splitlines())]

    return equations

def part1():
    equations = processing()
    sum = 0

    for equation in equations:
        result = equation[0]
        numbers = equation[1]

        # 0 = +   1 = *
        combinations = [list(combination) for combination in product([0, 1], repeat=len(numbers) - 1)]
        
        for combination in combinations:
            intermediate = numbers[0]

            for i in range(len(combination)):
                operation = combination[i]

                if operation == 0:
                    intermediate += numbers[i+1]
                
                else:
                    intermediate *= numbers[i+1]
            
            if intermediate == result:
                sum += result
                break
    
    return sum

def part2():
    equations = processing()
    sum = 0

    for equation in equations:
        result = equation[0]
        numbers = equation[1]

        # 0 = +  1 = *   2 = ||
        combinations = [list(combination) for combination in product([0, 1, 2], repeat=len(numbers) - 1)]
        
        for combination in combinations:
            intermediate = numbers[0]

            for i in range(len(combination)):
                operation = combination[i]

                if operation == 0:
                    intermediate += numbers[i+1]
                
                elif operation == 1:
                    intermediate *= numbers[i+1]
                
                else:
                    intermediate = int(str(intermediate) + str(numbers[i+1]))
            
            if intermediate == result:
                sum += result
                break
    
    return sum

if __name__ == "__main__":
    print(part1())
    print(part2())