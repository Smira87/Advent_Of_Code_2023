from collections import deque

ans = float("inf")
mappers = []

with open("05.data.txt") as file:
    line = file.readline().strip()
    _, data = line.split(":")
    data = data.strip()
    seeds = deque(int(_) for _ in data.split())
    for line in file:
        line = line.strip()
        if not line:
            continue
        if line[0].isalpha():
            mappers.append([])
            continue
        dst, src, count = (int(_) for _ in line.split())
        mappers[-1].append((src, dst, count))

next_seeds = deque()

for mapper in mappers:
    while seeds:
        seed_start, count = seeds.popleft(), seeds.popleft()

        intersected = False
        for src, dst, range_count in mapper:
            src_end = src + range_count - 1
            if src_end < seed_start or seed_start + count - 1 < src:
                continue

            new_seed_start = max(src, seed_start)

            if new_seed_start > seed_start:
                seeds.append(seed_start)
                seeds.append(new_seed_start - 1 - seed_start + 1)

            new_seed_end = min(src + range_count - 1, seed_start + count - 1)

            if new_seed_end < seed_start + count - 1:
                seeds.append(new_seed_end + 1)
                seeds.append(seed_start + count - 1 - new_seed_end - 1 + 1)

            new_count = new_seed_end - new_seed_start + 1

            next_seeds.append(dst - src + new_seed_start)
            next_seeds.append(new_count)

            intersected = True

        if not intersected:
            next_seeds.append(seed_start)
            next_seeds.append(count)

    seeds, next_seeds = next_seeds, deque()

for idx in range(0, len(seeds), 2):
    ans = min(ans, seeds[idx])

print(ans)


