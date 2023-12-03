
def count_calibration_values(file):
    Lines = file.readlines()
    sum = 0
    for line in Lines:
        for sym in line.strip():
            if sym.isdigit():
                num1 = str(sym)
                break
        for sym in line.strip()[::-1]:
            if sym.isdigit():
                num2 = str(sym)
                break
        sum += int(num1 + num2)
    return sum
file1 = open('Day_1_Input.txt', 'r')
print(count_calibration_values(file1))