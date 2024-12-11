
def parseFile():
    with open('input/input4.txt', 'r') as file:
        return [line.strip() for line in file]

def part1(lines):
    total = 0

    for row in range(len(lines)):
        for col in range(len(lines[0])):
            cur = lines[row][col]
            if cur == 'X':
                # right
                if lines[row][col+1:col+4] == 'MAS':
                    total += 1
                # left
                if lines[row][col-3:col] == 'SAM':
                    total += 1
                # up
                if row >= 3:
                    if lines[row-1][col] == 'M' \
                            and lines[row-2][col] == 'A' \
                            and lines[row-3][col] == 'S':
                        total += 1
                # down
                if row + 3 < len(lines):
                    if lines[row+1][col] == 'M' \
                            and lines[row+2][col] == 'A' \
                            and lines[row+3][col] == 'S':
                        total += 1
                # diag up left
                if row >= 3 and col >= 3:
                    if lines[row-1][col-1] == 'M' \
                            and lines[row-2][col-2] == 'A' \
                            and lines[row-3][col-3] == 'S':
                        total += 1
                # diag up right
                if row >= 3 and col + 3 < len(lines[0]):
                    if lines[row-1][col+1] == 'M' \
                            and lines[row-2][col+2] == 'A' \
                            and lines[row-3][col+3] == 'S':
                        total += 1
                # diag down right
                if row + 3 < len(lines) and col + 3 < len(lines[0]):
                    if lines[row+1][col+1] == 'M' \
                            and lines[row+2][col+2] == 'A' \
                            and lines[row+3][col+3] == 'S':
                        total += 1
                # diag down left
                if row + 3 < len(lines) and col >= 3:
                    if lines[row+1][col-1] == 'M' \
                            and lines[row+2][col-2] == 'A' \
                            and lines[row+3][col-3] == 'S':
                        total += 1

    return total

def part2(lines):
    total = 0

    for row in range(len(lines) - 2):
        for col in range(len(lines[0]) - 2):
            cur = lines[row][col]
            if cur == 'M' or cur == 'S':
                onRow = lines[row][col+2]
                if (onRow == 'M' or onRow == 'S') and lines[row+1][col+1] == 'A':
                    if cur == 'M' and onRow == 'M':
                        if lines[row+2][col] == 'S' and lines[row+2][col+2] == 'S':
                            total += 1
                    elif cur == 'S' and onRow == 'S':
                        if lines[row+2][col] == 'M' and lines[row+2][col+2] == 'M':
                            total += 1
                    else:
                        if lines[row+2][col] == cur and lines[row+2][col+2] == onRow:
                            total += 1

    return total

lines = parseFile()
# print(part1(lines))
print(part2(lines))

