
import re

def parseFile():
    with open('input/input3.txt', 'r') as file:
        return file.read()

def part1(file):
    pattern = r'mul\((\d\d?\d?),(\d\d?\d?)\)'
    muls = re.findall(pattern, file)
    return sum(map(lambda x: int(x[0]) * int(x[1]), muls))

def part2(file):
    pattern = r'mul\((\d\d?\d?),(\d\d?\d?)\)'
    total = 0

    start = 0
    end = file.find("don't()", start)

    while end != -1:
        muls = re.findall(pattern, file[start:end])
        total += sum(map(lambda x: int(x[0]) * int(x[1]), muls))

        start = file.find("do()", end)
        end = file.find("don't()", start)
        if start == -1:
            break

    if start != -1:
        muls = re.findall(pattern, file[start:])
        total += sum(map(lambda x: int(x[0]) * int(x[1]), muls))

    return total

file = parseFile()
# print(part1(file))
print(part2(file))

