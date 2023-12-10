
time_to_distance = []
total_count = 0
with open("06.data.txt") as file:
    for line in file:
        line = line.strip()
        if line[0] == "T":
            _, line = line.split(":")
            for idx, num in enumerate(line.split()):
                time_to_distance.append([int(num)])
        else:
            _, line = line.split(":")
            for idx, num in enumerate(line.split()):
                time_to_distance[idx].append(int(num))

def count_distance(hold_time, total_time):
    distance = (total_time - hold_time) * hold_time
    return distance

for time, dist in time_to_distance:
    count = 0
    for hold_time in range(time):
        if count_distance(hold_time, time) > dist:
            count += 1
    if not total_count:
        total_count = count
    else:
        total_count *= count
print(total_count)