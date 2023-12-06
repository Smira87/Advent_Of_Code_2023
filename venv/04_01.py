import re
import math

ans = 0

with open("04.data.txt") as file:
    for line in file:
        wins_list = []
        nums_list = []
        points = 0
        occurance = 0
        _, game = line.strip().split(": ")
        wins, nums = game.split(" | ")
        for match in re.finditer(r'\d+', wins):
            wins_list.append(int(match.group()))
        for match in re.finditer(r'\d+', nums):
            nums_list.append(int(match.group()))
        for num in wins_list:
            if num in nums_list:
                occurance += 1
        if occurance == 1:
            points = 1
        elif occurance > 1:
            points = 2 ** (occurance - 1)
        ans += points
print(ans)
