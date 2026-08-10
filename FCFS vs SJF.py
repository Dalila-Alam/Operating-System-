processes_sjf = [
    ["P1", 3, 3],
    ["P2", 2, 5],
    ["P3", 5, 4],
    ["P4", 1, 3],
    ["P5", 6, 2]
]

n = len(processes_sjf)

completed = []
current_time = 0
total_wt_sjf = 0
total_tat_sjf = 0
sjf_results = []
sjf_execution = []

print("========== SJF ==========")
print("Execution Order:")

while len(completed) < n:

    available = []


    for p in processes_sjf:
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
    tat = ct - at
    wt = tat - bt


    sjf_results.append([pid, at, bt, ct, tat, wt])
    sjf_execution.append(pid)

    completed.append(pid)
    current_time = ct

    total_wt_sjf += wt
    total_tat_sjf += tat

    print(pid, end=" -> ")

print("END")


print("\nSJF Table:")
print("PID\tAT\tBT\tCT\tTAT\tWT")

for p in sjf_results:
    print(
        f"{p[0]}\t"
        f"{p[1]}\t"
        f"{p[2]}\t"
        f"{p[3]}\t"
        f"{p[4]}\t"
        f"{p[5]}"
    )

average_wt_sjf = total_wt_sjf / n
average_tat_sjf = total_tat_sjf / n

print("\nAverage Waiting Time =", average_wt_sjf)
print("Average Turnaround Time =", average_tat_sjf)






processes_fcfs = [
    ["P0", 3, 3],
    ["P1", 2, 5],
    ["P2", 5, 4],
    ["P3", 1, 3],
    ["P4", 6, 2]
]


processes_fcfs.sort(key=lambda x: x[1])

time = 0
total_wt_fcfs = 0
total_tat_fcfs = 0
fcfs_execution = []

print("\n\n========== FCFS ==========")

print("Execution Order:")

for p in processes_fcfs:

    pid = p[0]
    at = p[1]
    bt = p[2]


    if time < at:
        time = at


    time = time + bt
    ct = time


    tat = ct - at


    wt = tat - bt

    total_tat_fcfs += tat
    total_wt_fcfs += wt

    fcfs_execution.append(pid)

    print(pid, end=" -> ")

print("END")


print("\nFCFS Table:")
print("PID\tAT\tBT\tCT\tTAT\tWT")


time = 0

for p in processes_fcfs:

    pid = p[0]
    at = p[1]
    bt = p[2]

    if time < at:
        time = at

    time = time + bt
    ct = time

    tat = ct - at
    wt = tat - bt

    print(
        f"{pid}\t"
        f"{at}\t"
        f"{bt}\t"
        f"{ct}\t"
        f"{tat}\t"
        f"{wt}"
    )


average_wt_fcfs = total_wt_fcfs / len(processes_fcfs)
average_tat_fcfs = total_tat_fcfs / len(processes_fcfs)

print("\nAverage Waiting Time =", average_wt_fcfs)
print("Average Turnaround Time =", average_tat_fcfs)









print("\t\tSJF\tFCFS")

print(
    "Average WT\t",
    round(average_wt_sjf, 2),
    "\t",
    round(average_wt_fcfs, 2)
)

print(
    "Average TAT\t",
    round(average_tat_sjf, 2),
    "\t",
    round(average_tat_fcfs, 2)
)



if average_wt_sjf < average_wt_fcfs:
    print("\nSJF has lower Average Waiting Time.")

elif average_wt_fcfs < average_wt_sjf:
    print("\nFCFS has lower Average Waiting Time.")

else:
    print("\nBoth SJF and FCFS have the same Average Waiting Time.")