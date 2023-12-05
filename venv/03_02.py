import re

ans = 0
data = []

with open("03.data.txt") as file:
    for line in file:
        line = "." + line.strip() + "."
        line_data = [line, [], []]
        for match in re.finditer(r'\d+', line):
            start, end, number = match.start(), match.end(), match.group()
            number = int(number)
            line_data[1].append([start, end - 1, number])
        for match in re.finditer(r'\*', line):
            start, star = match.start(), match.group()
            line_data[2].append(start)
        data.append(line_data)
data.insert(0, ['.' * len(data[0][0]), [], []])
data.append(['.' * len(data[0][0]), [], []])

def find_number(pos: int, numbers: list):
    for start, end, number in numbers:
        if start <= pos <= end:
            return number
    return -1

for idx, line in enumerate(data[1: len(data) -1], 1):
    line, numbers, stars = line
    for star in stars:
        adj_numbers = []

        #left
        if (number := find_number(star - 1, numbers)) >= 0:
            adj_numbers.append(number)
        #right

        if (number := find_number(star + 1, numbers)) >= 0:
            adj_numbers.append(number)

        #top center
        if (number := find_number(star, data[idx - 1][1])) >= 0:
            adj_numbers.append(number)
        else:
            #top left
            if (number := find_number(star - 1, data[idx - 1][1])) >= 0:
                adj_numbers.append(number)

            #top right
            if (number := find_number(star + 1, data[idx - 1][1])) >= 0:
                adj_numbers.append(number)
        #bottom center
        if (number := find_number(star, data[idx + 1][1])) >= 0:
            adj_numbers.append(number)
        else:
            #bottom left
            if (number := find_number(star - 1, data[idx + 1][1])) >= 0:
                adj_numbers.append(number)

            #bottom right
            if (number := find_number(star + 1, data[idx + 1][1])) >= 0:
                adj_numbers.append(number)

        if len(adj_numbers) == 2:
            ans += adj_numbers[1] * adj_numbers[0]

print(ans)