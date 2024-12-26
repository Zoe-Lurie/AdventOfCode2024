
from queue import SimpleQueue
import matplotlib.pyplot as plt
import helper

CHECKED = '.'

def parseFile():
    with open('input/input12.txt') as file:
        lines = [[c for c in line.rstrip()] for line in file]
        size = (len(lines), len(lines[0]))
        return lines, size

def part1(grid, size):
    total = 0
    for row in range(size[0]):
        for col in range(size[1]):
            c = grid[row][col]
            if c is not CHECKED:
                area = 1
                perimeter = 0
                q = SimpleQueue()
                q.put((row, col))
                grid[row][col] = CHECKED
                curRegion = {(row, col)}
                while not q.empty():
                    (nr, nc) = q.get()
                    for nbr in helper.neighborsNoCheck((nr, nc)):
                        if helper.outOfBounds(nbr, size):
                            perimeter += 1
                        else:
                            nchar = grid[nbr[0]][nbr[1]]
                            if nchar is not c and nbr not in curRegion:
                                perimeter += 1
                            elif nchar is c:
                                q.put(nbr)
                                area += 1
                                grid[nbr[0]][nbr[1]] = CHECKED
                                curRegion.add(nbr)
                total += area * perimeter

    return total

def addSide(row, col, dr, dc):
    if dr == 1:
        return ((row + 1, col), (row + 1, col + 1))
    if dr == -1:
        return ((row, col), (row, col + 1))
    if dc == 1:
        return ((row, col + 1), (row + 1, col + 1))
    if dc == -1:
        return ((row, col), (row + 1, col))

def countSides(sides):
    numSides = 0

    initialCoord1, initialCoord2 = None, None
    curCoord1, curCoord2 = None, None
    while sides:
        if not initialCoord1:
            (curCoord1, curCoord2) = sides.pop()
            initialCoord1, initialCoord2 = curCoord1, curCoord2
            numSides += 1
        for index, (c1, c2) in enumerate(sides):
            if c1 == curCoord2 or c2 == curCoord2:
                if c2 == curCoord2:
                    c1, c2 = c2, c1

                for (cn1, cn2) in sides[index + 1:]:
                    if cn1 == curCoord2 or cn2 == curCoord2:
                        if (curCoord1[0] == c1[0] and curCoord1[0] == c2[0]) or (curCoord1[1] == c1[1] and curCoord1[1] == c2[1]):
                            numSides += 2
                        break

                if not ((curCoord1[0] == c1[0] and curCoord1[0] == c2[0]) or (curCoord1[1] == c1[1] and curCoord1[1] == c2[1])):
                    numSides += 1

                sides.pop(index)
                if c2 == initialCoord1:
                    if (c1[0] == c2[0] and c1[0] == initialCoord2[0]) or (c1[1] == c2[1] and c1[1] == initialCoord2[1]):
                        numSides -= 1
                    initialCoord1, initialCoord2 = None, None
                else:
                    curCoord1, curCoord2 = c1, c2
                break

    return numSides

def showSides(sides):
    for side in sides:
        plt.plot([side[0][0], side[1][0]], [side[0][1], side[1][1]], 'b', linestyle='solid')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    # numSides = int(input('Enter number of sides: '))
    return 0

def part2(grid, size):
    total = 0
    for row in range(size[0]):
        for col in range(size[1]):
            c = grid[row][col]
            if c is not CHECKED:
                area = 1
                sides = []
                q = SimpleQueue()
                q.put((row, col))
                grid[row][col] = CHECKED
                curRegion = {(row, col)}
                while not q.empty():
                    (nr, nc) = q.get()
                    for (dr, dc) in helper.dirs:
                        nbr = (nr + dr, nc + dc)
                        if helper.outOfBounds(nbr, size):
                            sides.append(addSide(nr, nc, dr, dc))
                        else:
                            nchar = grid[nbr[0]][nbr[1]]
                            if nchar is not c and nbr not in curRegion:
                                sides.append(addSide(nr, nc, dr, dc))
                            elif nchar is c:
                                q.put(nbr)
                                area += 1
                                grid[nbr[0]][nbr[1]] = CHECKED
                                curRegion.add(nbr)
                numSides = countSides(sides)
                # numSides = countSides(sides.copy())
                total += area * numSides

                # print(f'{c}: {area} * {numSides} = {area * numSides}')
                # showSides(sides)

    return total

lines, size = parseFile()
# print(part1(lines, size))
print(part2(lines, size))

