
def parseFile():
    with open('input/input1.txt', 'r') as file:
        l1 = []
        l2 = []
        for line in file:
            line = line.split()
            l1.append(int(line[0]))
            l2.append(int(line[1]))
        return l1, l2

def part1(l1, l2):
    total = 0
    l1.sort()
    l2.sort()

    for a, b in zip(l1, l2):
        total += abs(a - b)

    return total

def part2(l1, l2):
    total = 0
    for n in l1:
        total += (n * l2.count(n))
    return total

l1, l2 = parseFile()
# print(part1(l1, l2))
print(part2(l1, l2))

