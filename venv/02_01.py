# only 12 red cubes, 13 green cubes, and 14 blue cubes

colors_map = {"r": 12, "g": 13, "b": 14}

file1 = open('02.data.txt', 'r')
ans = 0
game_N = 1
for line in file1:
    line = line.strip().split(":")[1]
    ans += game_N
    for idx in range(len(line)):
        if line[idx].isdigit() and line[idx + 1].isdigit():
            if int(line[idx] + line[idx + 1]) > colors_map[line[idx + 3]]:
                ans -= game_N
                break
    game_N += 1
print(ans)