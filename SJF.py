processes = [
    ["P1", 3, 3, 0, 0, 0],
    ["P2", 2, 5, 0, 0, 0],
    ["P3", 5, 4, 0, 0, 0],
    ["P4", 1, 3, 0, 0, 0],
    ["P5", 6, 2, 0, 0, 0]
]

n = len(processes)
completed = []
current_time = 0
total_wt = 0
total_tat = 0

print("Execution Order :")

while len(completed) < n:

    available = []

    for p in processes:
        if p[0] not in completed and p[1] <= current_time:
            available.append(p)

    if not available:
        current_time += 1
        continue

    selected = min(available, key=lambda x: x[2])

    pid = selected[0]
    at = selected[1]
    bt = selected[2]

    ct = current_time + bt
    wt = current_time - at
    tat = ct - at

    selected[3] = ct
    selected[4] = tat
    selected[5] = wt

    completed.append(pid)
    current_time = ct

    total_wt += wt
    total_tat += tat

    print(pid, end=" ")

print("\n")

print("PID\tAT\tBT\tCT\tTAT\tWT")

for p in processes:
    print(f"{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}\t{p[5]}")

average_wt = total_wt / n
average_tat = total_tat / n

print("Average WT :", average_wt)
print("Average TAT :", average_tat)
