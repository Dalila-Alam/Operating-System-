processes = [
    ["P0", 3, 1],
    ["P1", 5, 3],
    ["P2", 2, 2],
    ["P3", 1, 2],
    ["P4", 6, 3]
]

processes.sort(key=lambda x: x[1])

time = 0
total_wt = 0
total_tat = 0

print("PID\tAT\tBT\tCT\tTAT\tWT")

execution = []

for p in processes:
    pid = p[0]
    at = p[1]
    bt = p[2]

    if time < at:
        time = at

    time = time + bt
    ct = time
    tat = ct - at
    wt = tat - bt

    total_tat += tat
    total_wt += wt

    execution.append(pid)

    print(pid, "\t", at, "\t", bt, "\t", ct, "\t", tat, "\t", wt)

print("\nAverage Turnaround Time =", total_tat / len(processes))
print("Average Waiting Time =", total_wt / len(processes))

print("\nExecution Sequence:")
print(" -> ".join(execution))