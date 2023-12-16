from math import lcm

ans = 0
adj_nodes = {}

with open('08.data.txt') as file:
    lr = file.readline().strip()
    file.readline()
    for line in file:
        line = line.strip()
        source, nodes = line.split(" = ")
        adj_nodes[source] = nodes[1: -1].split(", ")

lr_len = len(lr)
nodes_ans = []

for node in [_ for _ in adj_nodes if _.endswith("A")]:
    node_ans = 0
    lr_idx = -1
    while not node.endswith('Z'):
        lr_idx += 1
        lr_idx %= lr_len
        move_idx = 'LR'.index(lr[lr_idx])
        node = adj_nodes[node][move_idx]
        node_ans += 1
    nodes_ans.append(node_ans)

ans = lcm(*nodes_ans)
print(ans)