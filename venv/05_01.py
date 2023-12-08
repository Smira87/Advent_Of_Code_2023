ans = float("inf")
mappers = []

with open("05.data.txt") as file:
    line = file.readline().strip()
    _, data = line.split(":")
    seeds = [ int(_) for _ in data.split()]
    for line in file:
        line = line.strip()
        if not line:
            continue
        if line[0].isalpha():
            mappers.append([])
            continue
        dst, src, count = (int(_) for _ in line.split())
        mappers[-1].append((src, dst, count))

for seed in seeds:
    for mapper in mappers:
        for src, dst, count in mapper:
            if src <= seed < src + count:
                seed = dst - src + seed
                break
    ans = min(ans, seed)

print(ans)