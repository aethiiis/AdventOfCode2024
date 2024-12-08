from itertools import permutations
from functools import cmp_to_key

def processing():
    with open("src/day05/input.txt") as file:
        twoparts = file.read().split("\n\n")
        rules = twoparts[0].split("\n")
        printers = twoparts[1].split("\n")
        
        # Rules
        global rules_dict
        global rules_list
        rules_list = []
        rules_dict = {}
        for rule in rules:
            rule = rule.split("|")

            num = int(rule[1])
            necessity = int(rule[0])
            
            if num in rules_dict:
                rules_dict[num].append(necessity)
            else:
                rules_dict[num] = [necessity]
            
            rules_list.append([num, necessity])

        # Printers
        printers_list = []
        for printer in printers:
            printers_list.append([int(num) for num in printer.split(",")])
        
        return printers_list, rules_dict

def part1():
    printers, rules = processing()

    correct_printers = []

    for printer in printers:
        if check_correct_printer(printer, rules):
            correct_printers.append(printer)

    sum = 0
    for i in range(len(correct_printers)):
        printer = correct_printers[i]
        sum += printer[len(printer)//2]
    
    return sum

def part2():
    printers, rules = processing()

    corrected_printers = []
    sorted_printers = []
    iterated_printers = printers[:]

    for printer in printers:
        if not check_correct_printer(printer, rules):
            corrected_printers.append(generate_correct_printer(printer, rules))
            sorted_printers.append(sorted(printer, key=cmp_to_key(compare)))
        else:
            iterated_printers.remove(printer)

    for i in range(len(rules_list)):
        num, necessity = rules_list[i]
        for j in range(len(iterated_printers)):
            printer = iterated_printers[j]
            if num in printer and necessity in printer:
                num_index = printer.index(num)
                necessity_index = printer.index(necessity)
                if num_index < necessity_index:
                    iterated_printers[j][num_index], iterated_printers[j][necessity_index] = iterated_printers[j][necessity_index], iterated_printers[j][num_index]
    
    #for i in range(len(iterated_printers)):
    #    if iterated_printers[i] != sorted_printers[i]:
    #        print(iterated_printers, sorted_printers)
    #        print("=")
            
    
    sum = 0
    for i in range(len(sorted_printers)):
        printer = iterated_printers[i]
        sum += printer[len(printer)//2]
    
    return sum

def check_correct_printer(printer, rules_dict):
    for i in range(len(printer)):
        num = printer[i]

        if num not in rules_dict:
            continue

        elif num in rules_dict:
            necessity = rules_dict[num]
            for need in necessity:
                if need in printer and need not in printer[:i]:
                    return False
    return True

def generate_correct_printer(printer, rules_dict):
    while not check_correct_printer(printer, rules_dict):
        for i in range(len(printer)):
            num = printer[i]

            if num not in rules_dict:
                continue

            elif num in rules_dict:
                necessity = rules_dict[num]
                for need in necessity:
                    if need in printer and need not in printer[:i]:
                        index_need = printer.index(need)
                        printer[i], printer[index_need] = printer[index_need], printer[i]
            
        return printer


def compare(num1, num2):
    if num1 in rules_dict:
        necessity = rules_dict[num1]
        if num2 in necessity:
            return True
    
    if num2 in rules_dict:
        necessity = rules_dict[num2]
        if num1 in necessity:
            return False
    
    return num1 > num2

if __name__ == "__main__":
    print(part1())
    print(part2())