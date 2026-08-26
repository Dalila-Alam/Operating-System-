
def sjf(processes, quantum):
    n = len(processes)
    remaining = [p[2] for p in processes]
    ct = [0] * n
    time = 0
    completed = 0

    while completed < n:
        ready = [i for i in range(n)
                 if processes[i][1] <= time and remaining[i] > 0]

        if not ready:
            time += 1
            continue

        i = min(ready, key=lambda x: remaining[x])

        run = min(quantum, remaining[i])
        remaining[i] -= run
        time += run

        if remaining[i] == 0:
            ct[i] = time
            completed += 1

    print("Process\tAT\tBT\tCT\tTAT\tWT")

    wt = []
    tat = []

    for i in range(n):
        t = ct[i] - processes[i][1]
        w = t - processes[i][2]
        tat.append(t)
        wt.append(w)

        print(f"{processes[i][0]}\t{processes[i][1]}\t"
              f"{processes[i][2]}\t{ct[i]}\t{t}\t{w}")

    print("Average WT:", sum(wt) / n)
    print("Average TAT:", sum(tat) / n)


processes = [
    ("P1", 4, 2),
    ("P2", 2, 2),
    ("P3", 1, 3),
    ("P4", 0, 6),
    ("P5", 3, 1)
]

sjf(processes, 2)
