
from queue import SimpleQueue

def parseFile():
    with open('input/input10.txt') as file:
        return [[int(c) for c in line.rstrip()] for line in file]

def neighbors(pos, size):
    nbrs = [(pos[0] + 1, pos[1]),
            (pos[0] - 1, pos[1]),
            (pos[0], pos[1] + 1),
            (pos[0], pos[1] - 1)]
    return [(r, c) for (r, c) in nbrs if r >= 0 and r < size[0] and c >= 0 and c < size[1]]

def bfs(grid, startRow, startCol, size):
    solutions = set()
    visited = set()
    q = SimpleQueue()
    q.put((startRow, startCol))

    while not q.empty():
        pos = q.get()
        n = grid[pos[0]][pos[1]]
        if n == 9:
            solutions.add(pos)
        else:
            for newPos in neighbors(pos, size):
                if grid[newPos[0]][newPos[1]] == n + 1 and newPos not in visited:
                    visited.add(newPos)
                    q.put(newPos)

    return len(solutions)

def part1(grid):
    size = (len(grid), len(grid[0]))
    sum = 0
    for row in range(size[0]):
        for col in range(size[1]):
            if grid[row][col] == 0:
                sum += bfs(grid, row, col, size)

    return sum

def rating(grid, startRow, startCol, size):
    numSolutions = 0
    q = SimpleQueue()
    q.put((startRow, startCol))

    while not q.empty():
        pos = q.get()
        n = grid[pos[0]][pos[1]]
        if n == 9:
            numSolutions += 1
        else:
            for newPos in neighbors(pos, size):
                if grid[newPos[0]][newPos[1]] == n + 1:
                    q.put(newPos)

    return numSolutions

def part2(grid):
    size = (len(grid), len(grid[0]))
    sum = 0
    for row in range(size[0]):
        for col in range(size[1]):
            if grid[row][col] == 0:
                sum += rating(grid, row, col, size)

    return sum

grid = parseFile()
# print(part1(grid))
print(part2(grid))

