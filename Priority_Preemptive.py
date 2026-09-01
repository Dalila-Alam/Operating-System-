p = [["P1",0,3,3],
   ["P2",1,4,2],
   ["P3",2,6,4],
   ["P4",3,4,6],
   ["P5",5,2,10]]

n=len(p)
rem=[x[2] for x in p]
time = 0
ct = [0] * n

while sum(rem) > 0 :
    ready = [
        i for i in range(n)
        if p[i][1] <= time and rem[i] > 0
    ]

    if not ready:
        time += 1
        continue


    i = min(ready, key=lambda x: p[x][3])

    rem[i] -= 1
    time += 1

    if rem[i] == 0:
        ct[i] = time

print("Process\tAT\tBT\tPriority\tCT\tTAT\tWT")

total_tat = total_wt = 0

for i in range(n):
    tat = ct[i] - p[i][1]
    wt = tat - p[i][2]

    total_tat += tat
    total_wt += wt

    print(
        f"{p[i][0]}\t{p[i][1]}\t{p[i][2]}\t"
        f"{p[i][3]}\t\t{ct[i]}\t{tat}\t{wt}"
    )

print("\nAverage TAT =", total_tat / len(p))
print("Average WT =", total_wt / len(p))
