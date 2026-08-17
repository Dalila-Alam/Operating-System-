processes = [
    ["P1", 0, 7],
    ["P2", 1, 4],
    ["P3", 2, 15],
    ["P4", 3, 11],
    ["P5", 4, 20],
    ["P6", 4 , 9]
]

quantum = 5

n = len(processes)
remaining = [p[2] for p in processes]
completion = [0] * n
time = 0
completed = 0
queue = []
visited = [False] * n
execution_order = []

while completed < n:

    for i in range(n):
        if processes[i][1] <= time and not visited[i] and remaining[i] > 0:
            queue.append(i)
            visited[i] = True

    if not queue:
        time += 1
        continue

    i = queue.pop(0)

    execution_order.append(processes[i][0])

    if remaining[i] > quantum:
        time += quantum
        remaining[i] -= quantum
    else:
        time += remaining[i]
        remaining[i] = 0
        completion[i] = time
        completed += 1

    for j in range(n):
        if processes[j][1] <= time and not visited[j] and remaining[j] > 0:
            queue.append(j)
            visited[j] = True

    if remaining[i] > 0:
        queue.append(i)

print("Execution Order:")
print(" -> ".join(execution_order))

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

total_wt = 0
total_tat = 0

for i in range(n):
    at = processes[i][1]
    bt = processes[i][2]
    ct = completion[i]

    tat = ct - at
    wt = tat - bt

    total_tat += tat
    total_wt += wt

    print(f"{processes[i][0]}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

print("\nAverage Waiting Time:", total_wt / n)
print("Average Turnaround Time:", total_tat / n)