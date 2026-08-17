def sjf(processes):
    n = len(processes)
    time = 0
    completed = 0
    done = [False] * n
    result = []

    while completed < n:
        idx = -1
        min_bt = float('inf')

        for i in range(n):
            pid, at, bt = processes[i]
            if at <= time and not done[i] and bt < min_bt:
                min_bt = bt
                idx = i

        if idx == -1:
            time += 1
            continue

        pid, at, bt = processes[idx]
        ct = time + bt
        tat = ct - at
        wt = tat - bt
        result.append((pid, at, bt, ct, tat, wt))

        time = ct
        done[idx] = True
        completed += 1

    return result


def show(result):
    print(f"{'PID':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")
    total_tat = total_wt = 0
    for pid, at, bt, ct, tat, wt in result:
        print(f"P{pid:<4}{at:<5}{bt:<5}{ct:<5}{tat:<5}{wt:<5}")
        total_tat += tat
        total_wt += wt

    n = len(result)
    print(f"\nAverage TAT: {total_tat/n:.2f}")
    print(f"Average WT: {total_wt/n:.2f}")


processes = [
    [1, 3, 2],
    [2, 2, 3],
    [3, 0, 2],
    [4, 1, 1],
    [5, 4, 5]
]

result = sjf(processes)
show(result)