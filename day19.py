
def parseFile():
    with open('input/input19.txt') as file:
        towels = {towel.strip() for towel in file.readline().split(',')}

        file.readline()

        patterns = []
        while line := file.readline():
            patterns.append(line.strip())

        return towels, patterns

def part1(towels, patterns):
    maxLen = max(map(len, towels))

    def testPattern(pattern, seen):
        if not pattern:
            return True

        if pattern in seen:
            return False

        for i in range(1, maxLen + 1):
            if pattern[:i] in towels and testPattern(pattern[i:], seen):
                return True

        seen.add(pattern)
        return False

    return sum([testPattern(pattern, set()) for pattern in patterns])

def part2(towels, patterns):
    maxLen = max(map(len, towels))

    def countPattern(pattern, memoizations):
        if not pattern:
            return 1

        if pattern in memoizations:
            return memoizations[pattern]

        total = 0
        for i in range(1, min(maxLen + 1, len(pattern) + 1)):
            if pattern[:i] in towels:
                total += countPattern(pattern[i:], memoizations)

        memoizations[pattern] = total
        return total

    return sum([countPattern(pattern, dict()) for pattern in patterns])

towels, patterns = parseFile()
# print(part1(towels, patterns))
print(part2(towels, patterns))

