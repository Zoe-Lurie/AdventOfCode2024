
import re
import time
from helper import neighbors

def parseFile():
    with open('input/input14.txt') as file:
        return [[int(s) for s in re.findall(r'-?\d+', line)] for line in file]

iterations = 100
width = 101
height = 103
# width = 11
# height = 7

def part1(robots):
    quadrantTotal = [0, 0, 0, 0]

    for sx, sy, dx, dy in robots:
        fx = sx + dx * iterations
        fy = sy + dy * iterations

        fx %= width
        fy %= height

        if fx < width // 2 and fy < height // 2:
            quadrantTotal[0] += 1
        elif fx < width // 2 and fy > height // 2:
            quadrantTotal[1] += 1
        elif fx > width // 2 and fy < height // 2:
            quadrantTotal[2] += 1
        elif fx > width // 2 and fy > height // 2:
            quadrantTotal[3] += 1

    return quadrantTotal[0] * quadrantTotal[1] * quadrantTotal[2] * quadrantTotal[3]

def part2(robots):
    i = 0
    while True:
        grid = [[' ' for _ in range(width)] for _ in range(height)]

        for sx, sy, dx, dy in robots:
            grid[sy][sx] = '#'

        count = 0
        for index, (sx, sy, dx, dy) in enumerate(robots):
            for (nx, ny) in neighbors((sx, sy), (width, height)):
                if grid[ny][nx] == '#':
                    count += 1
                    break

            robots[index][0] = (sx + dx) % width
            robots[index][1] = (sy + dy) % height

        if count > len(robots) // 2:
            print(i, '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            for row in grid:
                for c in row:
                    print(c, end='')
                print()

            time.sleep(0.5)

        i += 1

robots = parseFile()
# print(part1(robots))
print(part2(robots))

