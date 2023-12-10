
time_to_distance = []
total_count = 0
with open('06.data.txt') as file:
    _, data = file.readline().strip().split(':')
    time = [int(''.join(data.split()))]
    _, data = file.readline().strip().split(':')
    distance = [int(''.join(data.split()))]
def count_distance(hold_time, total_time):
    distance = (total_time - hold_time) * hold_time
    return distance

count = 0
for hold_time in range(time[0]):
    if count_distance(hold_time, time[0]) > distance[0]:
        count += 1
if not total_count:
    total_count = count
else:
    total_count *= count
print(total_count)