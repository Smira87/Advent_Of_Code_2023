
def count_calibration_values(file):
    digits_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5 \
        , "six": 6, "seven": 7, "eight": 8, "nine": 9}
    Lines = file.readlines()
    sum = 0
    for line in Lines:
        digits = []
        line = line.strip()
        for idx, letter in enumerate(line):
            if letter.isdigit():
                digits.append(int(letter))
                continue
            for word, digit in digits_map.items():
                if (idx + len(word)) <= len(line) and word == line[idx:idx + len(word)]:
                    digits.append(digit)
        sum += digits[0] * 10 + digits[-1]
    return sum

file1 = open('Input.txt', 'r')
print(count_calibration_values(file1))