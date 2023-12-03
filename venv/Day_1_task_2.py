import re

def modify_string(str):
    rep = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5" \
        , "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    return pattern.sub(lambda m: rep[re.escape(m.group(0))], str)

def count_calibration_values(file):
    Lines = file.readlines()
    sum = 0
    for line in Lines:
        modified_line = modify_string(line.strip())
        for sym in modified_line:
            if sym.isdigit():
                num1 = str(sym)
                break
        for sym in modified_line[::-1]:
            if sym.isdigit():
                num2 = str(sym)
                break
        sum += int(num1 + num2)
    return sum
file1 = open('Input.txt', 'r')
print(count_calibration_values(file1))