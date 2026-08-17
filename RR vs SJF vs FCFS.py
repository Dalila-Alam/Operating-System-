processes = [
    ["P1", 0, 7],
    ["P2", 1, 4],
    ["P3", 2, 15],
    ["P4", 3, 11],
    ["P5", 4, 20],
    ["P6", 4, 9]
]

quantum = 5


def fcfs(processes):
    time = 0
    results = []
    for p in processes:
        name, at, bt = p
        if time < at:
            time = at
        time += bt
        ct = time
        tat = ct - at
        wt = tat - bt
        results.append([name, at, bt, ct, tat, wt])
    return results


def sjf(processes):
    time = 0
    completed = []
    results = []
    while len(completed) < len(processes):
        available = []
        for i, p in enumerate(processes):
            if p[1] <= time and i not in completed:
                available.append((p[2], i))
        if not available:
            time += 1
            continue
        available.sort()
        i = available[0][1]
        name, at, bt = processes[i]
        time += bt
        ct = time
        tat = ct - at
        wt = tat - bt
        results.append([name, at, bt, ct, tat, wt])
        completed.append(i)
    return results


def round_robin(processes, quantum):
    n = len(processes)
    remaining = [p[2] for p in processes]
    completion = [0] * n
    queue = []
    visited = [False] * n
    time = 0
    completed = 0

    while completed < n:
        for i in range(n):
            if processes[i][1] <= time and not visited[i]:
                queue.append(i)
                visited[i] = True

        if not queue:
            time += 1
            continue

        i = queue.pop(0)
        if remaining[i] > quantum:
            time += quantum
            remaining[i] -= quantum
        else:
            time += remaining[i]
            remaining[i] = 0
            completion[i] = time
            completed += 1

        for j in range(n):
            if processes[j][1] <= time and not visited[j]:
                queue.append(j)
                visited[j] = True

        if remaining[i] > 0:
            queue.append(i)

    results = []
    for i in range(n):
        name, at, bt = processes[i]
        ct = completion[i]
        tat = ct - at
        wt = tat - bt
        results.append([name, at, bt, ct, tat, wt])
    return results


def display(name, results):
    print(f"\n{name}")
    print(f"{'Process':<8}{'AT':<6}{'BT':<6}{'CT':<6}{'TAT':<6}{'WT':<6}")

    total_wt = 0
    total_tat = 0
    for r in results:
        print(f"{r[0]:<8}{r[1]:<6}{r[2]:<6}{r[3]:<6}{r[4]:<6}{r[5]:<6}")
        total_wt += r[5]
        total_tat += r[4]

    print(f"Average WT : {total_wt / len(results):.2f}")
    print(f"Average TAT: {total_tat / len(results):.2f}")


fcfs_result = fcfs(processes)
sjf_result = sjf(processes)
rr_result = round_robin(processes, quantum)

display("FCFS", fcfs_result)
display("SJF", sjf_result)
display("Round Robin", rr_result)