
def parseFile():
    with open('input/input2.txt', 'r') as file:
        lines = [list(map(int, line.split())) for line in file]
        return lines

def checkSafe(line):
    n = line[0]
    increasing = None
    safe = True
    for i in range(1, len(line)):
        m = line[i]
        if abs(m - n) < 1 or abs(m - n) > 3:
            safe = False
            break
        if increasing is None:
            if m - n > 0:
                increasing = True
            else:
                increasing = False
        else:
            if (increasing and m - n < 0) or ((not increasing) and m - n > 0):
                safe = False
                break
        n = m

    return safe

def part1(lines):
    total = 0

    for line in lines:
        if checkSafe(line):
            total += 1

    return total

def part2(lines):
    total = 0

    for line in lines:
        if checkSafe(line):
            total += 1
        else:
            for i in range(len(line)):
                newLine = line[:i] + line[i+1:]
                if checkSafe(newLine):
                    total += 1
                    break

    return total

lines = parseFile()
# print(part1(lines))
print(part2(lines))

