
dirs = (1, 0), (-1, 0), (0, 1), (0, -1)

def outOfBounds(pos, size):
    return pos[0] < 0 or pos[0] >= size[0] or pos[1] < 0 or pos[1] >= size[1]

def neighbors(pos, size):
    nbrs = [(pos[0] + dx, pos[1] + dy) for (dx, dy) in dirs]
    return [(r, c) for (r, c) in nbrs if r >= 0 and r < size[0] and c >= 0 and c < size[1]]

def neighborsNoCheck(pos):
    return [(pos[0] + dx, pos[1] + dy) for (dx, dy) in dirs]

