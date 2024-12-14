
def parseFile():
    with open('input/input8.txt') as file:
        antennas = dict()

        width = None
        row = 0
        for line in file:
            line = line.strip()
            col = 0
            for c in line:
                if c != '.':
                    if c in antennas:
                        antennas[c] = antennas[c] + [(row, col)]
                    else:
                        antennas[c] = [(row, col)]
                col += 1
            width = col
            row += 1

        return antennas, (row, width)

def outOfBounds(pos, size):
    return pos[0] < 0 or pos[0] >= size[0] or pos[1] < 0 or pos[1] >= size[1]

def part1(antennas, size):
    antinodes = set()

    for c in antennas:
        locations = antennas[c]

        for i in range(len(locations)):
            l1 = locations[i]
            for l2 in locations[i+1:]:
                rowDistance = l1[0] - l2[0]
                colDistance = l1[1] - l2[1]

                a1 = (l1[0] + rowDistance, l1[1] + colDistance)
                a2 = (l2[0] - rowDistance, l2[1] - colDistance)

                if not outOfBounds(a1, size):
                    antinodes.add(a1)
                if not outOfBounds(a2, size):
                    antinodes.add(a2)

    return len(antinodes)

def part2(antennas, size):
    antinodes = set()

    for c in antennas:
        locations = antennas[c]

        for i in range(len(locations)):
            l1 = locations[i]
            for l2 in locations[i+1:]:
                rowDistance = l1[0] - l2[0]
                colDistance = l1[1] - l2[1]

                i = 0
                while not outOfBounds(a := (l1[0] + i * rowDistance, l1[1] + i * colDistance), size):
                    antinodes.add(a)
                    i += 1

                i = 0
                while not outOfBounds(a := (l1[0] - i * rowDistance, l1[1] - i * colDistance), size):
                    antinodes.add(a)
                    i += 1

    return len(antinodes)

antennas, size = parseFile()
# print(part1(antennas, size))
print(part2(antennas, size))

