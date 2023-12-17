ans = 0
seqs = []
with open("09.data.txt") as file:
    for line in file:
        line = line.strip()
        seqs.append([int(_) for _ in line.split()])

for seq in seqs:
    stack = [seq]
    while any(stack[-1]):
        curr_stack = stack[-1]
        next_stack = []
        for idx in range(1, len(curr_stack)):
            next_stack.append(curr_stack[idx] - curr_stack[idx - 1])
        stack.append(next_stack)
    next_num = 0
    while stack:
        next_num += stack.pop().pop()
    ans += next_num

print(ans)