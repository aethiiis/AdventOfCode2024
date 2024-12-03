import re

def processing():
    with open("src/day03/input.txt", "r") as input:
        lines = input.readlines()
        text = "".join(lines)

        pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
        matches = re.findall(pattern, text)

        nums = []
        for match in matches:
            
            if match == "do()":
                nums.append(1)
            
            elif match == "don't()":
                nums.append(0)
            
            elif match.startswith("mul("):
                nums.append([int(num) for num in match[4:-1].split(",")])
        
        return nums

def part1():
    nums = processing()
    count = 0

    for couple in nums:
        if couple != 0 and couple != 1:
            count += couple[0] * couple[1]
    
    return count

def part2():
    nums = processing()
    count = 0
    enabled = True

    for couple in nums:
        if couple == 0:
            enabled = False
        
        elif couple == 1:
            enabled = True
        
        elif enabled:
            count += couple[0] * couple[1]
        
    return count

if __name__ == "__main__":
    print(part1())
    print(part2())