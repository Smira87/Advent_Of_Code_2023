# only 12 red cubes, 13 green cubes, and 14 blue cubes

colors_map = {"red": 12, "green": 13, "blue": 14}

file1 = open('02.data.txt', 'r')
ans = 0

for line in file1:
    game, turn = line.strip().split(": ")
    game = game.split()[1]
    possible = True

    for move in turn.split("; "):
        for singe_move in move.split(", "):
            number, color = singe_move.split()
            if int(number) > colors_map[color]:
                possible = False
    if possible:
        ans += int(game)

print(ans)