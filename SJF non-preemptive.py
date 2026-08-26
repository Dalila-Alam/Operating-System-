def sjf(processes):
    n = len(processes)
    time = 0
    done = [False] * n
    results = []

    while len(results) < n:
        idx = -1
        min_bt = float('inf')
        for i in range(n):
            at, bt = processes[i][1], processes[i][2]
            if at <= time and not done[i] and bt < min_bt:
                min_bt = bt
                idx = i

        if idx == -1:
            time += 1
            continue

        name, at, bt = processes[idx]
        time += bt
        tat = time - at
        wt = tat - bt
        results.append([name, at, bt, time, tat, wt])
        done[idx] = True

    return results


processes = [
    ["P1", 0, 16],
    ["P2", 1, 5],
    ["P3", 2, 6],
    ["P4", 3, 1],
    ["P5", 4, 2]
]

results = sjf(processes)

print(f"{'P':<4}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")
total_tat = total_wt = 0
for r in results:
    print(f"{r[0]:<4}{r[1]:<5}{r[2]:<5}{r[3]:<5}{r[4]:<5}{r[5]:<5}")
    total_tat += r[4]
    total_wt += r[5]

print(f"\nAverage TAT: {total_tat / len(results):.2f}")
print(f"Average WT : {total_wt / len(results):.2f}")