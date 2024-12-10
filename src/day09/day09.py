def part1() -> int:
    disk_map = open("src/day09/input.txt").read()
    disk:list[int] = []
    blanks:list[int] = []

    pos:int = 0

    for i, char in enumerate(disk_map):
        x = int(char)
        if i%2 == 0:
            disk += [i//2] * x
        
        else:
            disk += [-1] * x
    
    blanks = [i for i, x in enumerate(disk) if x == -1]

    for i in blanks:
        while disk[-1] == -1: # removes end of string -1
            disk.pop()
        
        if len(disk) <= i: # for the case of 0...1 -> 01... -> 01 <= stop it here
            break

        disk[i] = disk.pop()

    return sum(i * x for i, x in enumerate(disk))

def part2() -> int:
    disk_map = open("src/day09/input.txt").read()
    files:dict[int, tuple[int, int]] = {}
    blanks:list[int] = []

    fid:int = 0
    pos:int = 0

    for i, char in enumerate(disk_map):
        x = int(char)
        if i%2 == 0:
            files[fid] = (pos, x)
            fid += 1

        else:
            if x != 0:
                blanks.append((pos, x))
        
        pos += x
    
    while fid > 0:
        fid -= 1
        pos, size = files[fid]

        for i, (start, length) in enumerate(blanks):

            if start >= pos:
                blanks = blanks[:i]
                break

            if size <= length:
                files[fid] = (start, size)

                if size == length:
                    blanks.pop(i)
                
                else:
                    blanks[i] = (start + size, length - size)
                
                break
    
    #return sum((value * (pos + i)) for value, (pos, size) in files.items() for i in range(size))
    return sum(fid * size * (2 * pos + size - 1) // 2 for fid, (pos, size) in files.items())

if __name__ == "__main__":
    print(part1())
    print(part2())