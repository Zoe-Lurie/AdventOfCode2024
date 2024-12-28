
def parseFile():
    with open('input/input13.txt') as file:
        linesString = file.read()
        lines = linesString.split('\n\n')
        lines = [line.split('\n') for line in lines]
        games = []
        for line in lines:
            b1x = int(line[0][line[0].find('+') + 1:line[0].find(',')])
            b1y = int(line[0][line[0].find('Y') + 2:])
            b2x = int(line[1][line[1].find('+') + 1:line[1].find(',')])
            b2y = int(line[1][line[1].find('Y') + 2:])
            px = int(line[2][line[2].find('=') + 1:line[2].find(',')])
            py = int(line[2][line[2].find('Y') + 2:])
            g = ((b1x, b1y), (b2x, b2y), (px, py))
            games.append(g)
        return games

def part1(games):
    total = 0
    for (ax, ay), (bx, by), (px, py) in games:
        t = None

        for n in range(0, 101):
            lx = px - ax * n
            ly = py - ay * n

            if lx % bx == 0 and ly % by == 0:
                if (m := lx // bx) == ly // by:
                    tt = 3 * n + m
                    if t is None or tt < t:
                        t = tt

        if t is not None:
            total += t

    return total

def part2(games):
    total = 0
    TOADD = 10000000000000
    for (ax, ay), (bx, by), (px, py) in games:
        px += TOADD
        py += TOADD

        r = ay / ax

        by2 = by - r * bx
        py2 = py - r * px

        if by2 == 0:
            print('zero row')
            continue

        bx2 = bx / ax
        px2 = px / ax

        py2 /= by2

        px2 -= bx2 * py2

        if px2 >= 0 and py2 >= 0:
            n = round(px2)
            m = round(py2)
            if ax * n + bx * m == px and ay * n + by * m == py:
                total += n * 3 + m

    return total

games = parseFile()
# print(part1(games))
print(part2(games))

# ax * n + bx * m = px
# ay * n + by * m = py
# t = 3 * n + m

# ax bx px
# ay by py
#
# ax bx px
# 0 by py
#
# 1 bx px
# 0 1 py
#
# 1 0 px
# 0 1 py

