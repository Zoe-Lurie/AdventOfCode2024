
def parseFile():
    with open('input/input6.txt', 'r') as file:
        obstacles = set()
        start = None
        row = 0
        width = None
        for line in file:
            line = line.strip()
            col = 0
            for c in line:
                if c == '#':
                    obstacles.add((row, col))
                elif c == '^':
                    start = ((row, col), (-1, 0))
                elif c == 'v':
                    start = ((row, col), (1, 0))
                elif c == '>':
                    start = ((row, col), (0, 1))
                elif c == '<':
                    start = ((row, col), (0, -1))

                col += 1

            width = col
            row += 1

        return obstacles, start, (row, width)

def outOfBounds(pos, size):
    if pos[0] < 0 or pos[0] >= size[0] or pos[1] < 0 or pos[1] >= size[1]:
        return True
    return False

def turnRight(dir):
    if dir == (-1, 0):
        return (0, 1)
    if dir == (0, 1):
        return (1, 0)
    if dir == (1, 0):
        return (0, -1)
    return (-1, 0)

def part1(obstacles, start, size):
    positions = set()
    pos = start[0]
    dir = start[1]

    while not outOfBounds(pos, size):
        positions.add(pos)
        newPos = (pos[0] + dir[0], pos[1] + dir[1])
        if newPos in obstacles:
            dir = turnRight(dir)
        else:
            pos = newPos

    return len(positions)

def part2Help(obstacles, start, size):
    positions = set()
    pos = start[0]
    dir = start[1]

    while not outOfBounds(pos, size):
        if (pos, dir) in positions:
            return True
        positions.add((pos, dir))
        newPos = (pos[0] + dir[0], pos[1] + dir[1])
        if newPos in obstacles:
            dir = turnRight(dir)
        else:
            pos = newPos
    return False

def part2(obstacles, start, size):
    positions = set()
    pos = start[0]
    dir = start[1]

    while not outOfBounds(pos, size):
        positions.add(pos)
        newPos = (pos[0] + dir[0], pos[1] + dir[1])
        if newPos in obstacles:
            dir = turnRight(dir)
        else:
            pos = newPos

    total = 0
    positions.discard(start[0])
    for pos in positions:
        obstacles.add(pos)
        if part2Help(obstacles, start, size):
            total += 1
        obstacles.remove(pos)

    return total

obstacles, start, size = parseFile()
# print(part1(obstacles, start, size))
print(part2(obstacles, start, size))

