import re

ans = 0
data = []

with open("03.data.txt") as file:
    for line in file:
        line = "." + line.strip() + "."
        line_data = [line, []]
        for match in re.finditer(r'\d+', line):
            start, end, number = match.start(), match.end(), match.group()
            number = int(number)
            line_data[1].append([start - 1, end, number])
        data.append(line_data)
data.insert(0, ["." * len(data[0][0]), []])
data.append(["." * len(data[0][0]), []])

for idx, line in enumerate(data[1: len(data) -1], 1):
    line, numbers = line
    for start, end, number in numbers:
        prev_line, next_line = data[idx - 1][0], data[idx + 1][0]
        if line[start] != "." or line[end] != "." or \
            prev_line[start:end + 1] != "." * (end - start + 1) or \
                next_line[start:end + 1] != "." * (end - start + 1):
            ans += number
print(ans)
