
def parseFile():
    with open('input/input7.txt') as file:
        return [((nums := [int(n) for n in line.replace(':', '').split()])[0], nums[1:]) for line in file]

def part1(lines):
    total = 0

    for result, nums in lines:
        possibleResults = [nums[0]]

        for n in nums[1:]:
            possibleResults = [n + r for r in possibleResults if n + r <= result] \
                + [n * r for r in possibleResults if n * r <= result]

        if result in possibleResults:
            total += result

    return total

def part2(lines):
    total = 0

    for result, nums in lines:
        possibleResults = [nums[0]]

        for n in nums[1:]:
            possibleResults = [n + r for r in possibleResults if n + r <= result] \
                + [n * r for r in possibleResults if n * r <= result] \
                + [int(str(r) + str(n)) for r in possibleResults if int(str(r) + str(n)) <= result]

        if result in possibleResults:
            total += result

    return total

lines = parseFile()
# print(part1(lines))
print(part2(lines))

