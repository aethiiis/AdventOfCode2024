def processing():
    disk_map = open("src/day09/input.txt").read()
    
    disk = []

    for i in range(len(disk_map)):
        if i%2 == 0:
            for _ in range(int(disk_map[i])):
                disk.append(i//2)

        else:
            for _ in range(int(disk_map[i])):
                disk.append(".")
    
    #print(disk[::-1])
    return disk, disk_map

def checksum(disk):
    sum = 0
    for i in range(len(disk)):
        if disk[i] == ".":
            continue
        sum += i * disk[i]
    
    return sum

def find_position_blocks(blocks, gaps):
    positions = [(0, blocks[0])]
    blocks = blocks[1:]

    while len(blocks) != 0:
        positions.append((positions[-1][1] + gaps[0], positions[-1][1] + gaps[0] + blocks[0]))
        blocks = blocks[1:]
        gaps = gaps[1:]

    return positions

def part1():
    disk, _ = processing()

    incomplete = True

    free:int
    last_free = 0
    move:int
    last_move = len(disk) - 1

    while incomplete:
        # Trouver un espace libre
        for i in range(last_free, len(disk), 1):
            if disk[i] == ".":
                free = i
                break
        
        # Trouver un chiffre à déplacer
        for i in range(last_move, -1, -1):
            if disk[i] != ".":
                move = i
                break

        if free > move:
            incomplete = False
        else:
            last_free = free
            last_move = move

            disk[free], disk[move] = disk[move], disk[free]
    
    return checksum(disk)
    
def part2():
    disk, disk_map = processing()
    gaps = list(map(int, disk_map[1::2]))
    blocks = list(map(int, disk_map[::2]))

    positions = find_position_blocks(blocks, gaps)
    for i in range(len(blocks)-1, -1, -1):
        block = blocks[i]

        gap_count = 0
        for j in range(0, len(disk), 1):
            if disk[j] == ".":
                gap_count += 1
            
                if gap_count == block and j-block+1 < positions[i][0]:
                    disk[j-block+1:j+1], disk[positions[i][0]:positions[i][1]] = disk[positions[i][0]:positions[i][1]], disk[j-block+1:j+1]
                    break
            
            else:
                gap_count = 0
    
    return checksum(disk)

if __name__ == "__main__":
    print(part1())
    print(part2())