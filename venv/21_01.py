from collections import deque

ans = 0
fields = []

with open('21.data.txt') as file:
    for line in file:
        line = line.strip()
        if 'S' in line:
            start = (len(fields) + 1, line.index('S') + 1)
        line = ("#" + line + "#")
        fields.append(line)
    fields.insert(0, "#" * len(fields[0]))
    fields.append("#" * len(fields[0]))
q = deque()
q.append(start)
for i in range(64):
    new_q = deque()
    visited = set()
    while q:
        pos = q.popleft()
        for col, row in (
                (pos[0] + 1, pos[1]),
                (pos[0] - 1, pos[1]),
                (pos[0], pos[1] + 1),
                (pos[0], pos[1] - 1),
        ):
            if (col, row) in visited or fields[row][col] == '#':
                continue
            new_q.append((col, row))
            visited.add((col, row))

    q = new_q
print(len(visited))