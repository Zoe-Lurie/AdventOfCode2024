
from queue import Queue
from helper import neighbors

def parseFile():
    with open('input/input18.txt') as file:
        return [[int(n) for n in line.split(',')] for line in file]

def part1(bytes):
    bytes = bytes[:1024]

    q = Queue()
    visited = set()

    for row, col in bytes:
        visited.add((row, col))

    q.put((0, 0, 0))
    visited.add((0, 0))

    while not q.empty():
        row, col, steps = q.get()

        if row == 70 and col == 70:
            return steps

        for nr, nc in neighbors((row, col), (71, 71)):
            if (nr, nc) not in visited:
                q.put((nr, nc, steps + 1))
                visited.add((nr, nc))

def part2(bytes):
    for i in range(len(bytes)):
        stack = []
        visited = set()

        for row, col in bytes[:i]:
            visited.add((row, col))

        stack.append((0, 0))

        while stack:
            row, col = stack.pop()

            if row == 70 and col == 70:
                break

            for nr, nc in neighbors((row, col), (71, 71)):
                if (nr, nc) not in visited:
                    stack.append((nr, nc))
                    visited.add((nr, nc))

        else:
            return bytes[i - 1]

bytes = parseFile()
# print(part1(bytes))
print(part2(bytes))

