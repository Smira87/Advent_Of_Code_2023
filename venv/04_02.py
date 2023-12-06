from collections import defaultdict

ans = 0
copies = defaultdict(int)
with open("04.data.txt") as file:
    for idx, line in enumerate(file):
        line = line.strip()
        _, data = line.split(": ")
        win, comb = data.split(" | ")
        win, comb = set(map(int, win.split())), set(map(int, comb.split()))
        matches = len(win & comb)
        for offset in range(matches):
            copies[idx + offset + 1] += 1 + copies[idx]
        ans += 1 + copies[idx]

print(ans)