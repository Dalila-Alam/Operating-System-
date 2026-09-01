p = [
    ["P1", 0, 3, 3],
    ["P2", 1, 4, 2],
    ["P3", 2, 6, 4],
    ["P4", 3, 4, 6],
    ["P5", 5, 2, 10],
]

n = len(p)


def non_preemptive_priority(p):
    time = 0
    done = []
    ct = [0] * n

    while len(done) < n:
        ready = [i for i in range(n) if p[i][1] <= time and i not in done]

        if not ready:
            time += 1
            continue

        i = min(ready, key=lambda x: p[x][3])

        time += p[i][2]
        ct[i] = time
        done.append(i)

    return ct


def preemptive_priority(p, quantum=1):
    remaining = [row[2] for row in p]
    ct = [0] * n
    time = 0
    completed = 0

    while completed < n:
        ready = [i for i in range(n) if p[i][1] <= time and remaining[i] > 0]

        if not ready:
            time += 1
            continue

        i = min(ready, key=lambda x: p[x][3])

        run = min(quantum, remaining[i])
        remaining[i] -= run
        time += run

        if remaining[i] == 0:
            ct[i] = time
            completed += 1

    return ct


def averages(ct):
    total_tat = total_wt = 0

    for i in range(n):
        tat = ct[i] - p[i][1]
        wt = tat - p[i][2]
        total_tat += tat
        total_wt += wt

    return total_tat / n, total_wt / n


avg_tat_np, avg_wt_np = averages(non_preemptive_priority(p))
avg_tat_p, avg_wt_p = averages(preemptive_priority(p, quantum=1))

print("Approach\t\tAvg TAT\tAvg WT")
print(f"Non-preemptive\t\t{avg_tat_np}\t{avg_wt_np}")
print(f"Preemptive (q=1)\t{avg_tat_p}\t{avg_wt_p}")

if avg_wt_np < avg_wt_p:
    print("\nNon-preemptive priority scheduling is better for this process set.")
elif avg_wt_p < avg_wt_np:
    print("\nPreemptive priority scheduling is better for this process set.")
else:
    print("\nBoth approaches perform equally for this process set.")