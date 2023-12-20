from collections import deque

ans = 0
tiles = []

with open("10.data.txt") as file:
    for line in file:
        line = line.strip()
        if 'S' in line:
            start = (line.index('S'), len(tiles), 0)
        tiles.append(line)

maps = {
    '|': ((0, -1), (0, 1)),
    '-': ((-1, 0), (1, 0)),
    'L': ((0, -1), (1, 0)),
    'J': ((0, -1), (-1, 0)),
    '7': ((-1, 0), (0, 1)),
    'F': ((1, 0), (0, 1)),
    'S': (((1, 0), (-1, 0)))
}

visited = set()
q = deque([start])

while q:
    curr = q.popleft()
    ans = max(ans, curr[2])
    visited.add((curr[0], curr[1]))
    for mapper in maps[tiles[curr[1]][curr[0]]]:
        next_pos = (curr[0] + mapper[0], curr[1] + mapper[1], curr[2] + 1)
        if (next_pos[0], next_pos[1]) in visited:
            continue
        q.append(next_pos)
print(ans)

