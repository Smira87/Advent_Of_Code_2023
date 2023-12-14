ans = 0
adj_nodes = {}

with open('08.data.txt') as file:
    lr = file.readline().strip()
    file.readline()
    for line in file:
        line = line.strip()
        source, nodes = line.split(" = ")
        adj_nodes[source] = nodes[1: -1].split(", ")
lr_idx, lr_len = -1, len(lr)
node = "AAA"
while node != "ZZZ":
    lr_idx += 1
    lr_idx %= lr_len
    move_idx = 'LR'.index(lr[lr_idx])
    node = adj_nodes[node][move_idx]
    ans += 1
print(ans)
