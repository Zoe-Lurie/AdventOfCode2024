
from helper import dirs
from queue import PriorityQueue

def parseFile():
    with open('input/input16.txt') as file:
        return [line for line in file]

def part1(maze):
    size = (len(maze), len(maze[0]))

    startPos = None
    for i, line in enumerate(maze):
        j = line.find('S')
        if j != -1:
            startPos = (i, j)

    visited = set()
    q = PriorityQueue()

    visited.add((startPos, (0, 1)))
    q.put((0, startPos, (0, 1)))

    while not q.empty():
        score, (cr, cc), (cdr, cdc) = q.get()

        if maze[cr][cc] == 'E':
            return score

        for dr, dc in dirs:
            nr = cr + dr
            nc = cc + dc

            if nr >= 0 and nr < size[0] and nc >= 0 and nc < size[1] \
                    and maze[nr][nc] != '#' and ((nr, nc), (dr, dc)) not in visited:
                newScore = score + (1 if dr == cdr and dc == cdc else 1001)
                q.put((newScore, (nr, nc), (dr, dc)))
                visited.add(((nr, nc), (dr, dc)))

def part2(maze):
    size = (len(maze), len(maze[0]))

    startPos = None
    for i, line in enumerate(maze):
        j = line.find('S')
        if j != -1:
            startPos = (i, j)

    visited = dict()
    q = []

    visited[(startPos, (0, 1))] = 0
    q.append((0, startPos, (0, 1), {(startPos, (0, 1))}))

    minTotalScore = None
    finalTilesOnPath = set()

    while q:
        minScore = None
        minIndex = None

        for i, (s, _, _, _) in enumerate(q):
            if not minScore or s < minScore:
                minScore = s
                minIndex = i

        score, (cr, cc), (cdr, cdc), tilesOnPath = q.pop(minIndex)

        if minTotalScore and score > minTotalScore:
            return len({x[0] for x in finalTilesOnPath})

        if maze[cr][cc] == 'E':
            if not minTotalScore:
                minTotalScore = score

            finalTilesOnPath.update(tilesOnPath)

        for dr, dc in dirs:
            nr = cr + dr
            nc = cc + dc

            if nr >= 0 and nr < size[0] and nc >= 0 and nc < size[1] \
                    and maze[nr][nc] != '#':
                newScore = score + (1 if dr == cdr and dc == cdc else 1001)

                if ((nr, nc), (dr, dc)) in visited and newScore == visited[((nr, nc), (dr, dc))]:
                    if ((nr, nc), (dr, dc)) in finalTilesOnPath:
                        finalTilesOnPath.update(tilesOnPath)
                    else:
                        for _, _, _, t in q:
                            if ((nr, nc), (dr, dc)) in t:
                                t.update(tilesOnPath)
                                break

                elif ((nr, nc), (dr, dc)) not in visited:
                    q.append((newScore, (nr, nc), (dr, dc), tilesOnPath | {((nr, nc), (dr, dc))}))
                    visited[((nr, nc), (dr, dc))] = newScore

maze = parseFile()
# print(part1(maze))
print(part2(maze))

