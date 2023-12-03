# only 12 red cubes, 13 green cubes, and 14 blue cubes

file1 = open('02.data.txt', 'r')
ans = 0

for line in file1:
    game, turn = line.strip().split(": ")
    game = game.split()[1]
    possible = True
    local_map = {"red": 0, "green": 0, "blue": 0}
    for move in turn.split("; "):
        for singe_move in move.split(", "):
            number, color = singe_move.split()
            if int(number) > local_map[color]:
                local_map[color] = int(number)
    mult = 1
    for key in local_map:
        mult *= local_map[key]
    ans += mult
print(ans)