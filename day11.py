
def parseFile():
    with open('input/input11.txt') as file:
        return [int(n) for n in file.read().split()]

def part1(stones):
    for _ in range(25):
        newStones = []
        for stone in stones:
            if stone == 0:
                newStones.append(1)
            elif ((ln := len(s := str(stone))) % 2) == 0:
                newStones.append(int(s[:ln // 2]))
                newStones.append(int(s[ln // 2:]))
            else:
                newStones.append(stone * 2024)
        stones = newStones

    return len(stones)

def part2Help(stone, n, memoizations):
    if n == 0:
        return 1
    if (stone, n) in memoizations:
        return memoizations[(stone, n)]
    total = 0
    if stone == 0:
        total += part2Help(1, n - 1, memoizations)
    elif ((ln := len(s := str(stone))) % 2) == 0:
        total += part2Help(int(s[:ln // 2]), n - 1, memoizations)
        total += part2Help(int(s[ln // 2:]), n - 1, memoizations)
    else:
        total += part2Help(stone * 2024, n - 1, memoizations)
    memoizations[(stone, n)] = total
    return total

def part2(stones):
    n = 75
    total = 0
    memoizations = dict()
    total = sum([part2Help(stone, n, memoizations) for stone in stones])

    return total


stones = parseFile()
# print(part1(stones))
print(part2(stones))

