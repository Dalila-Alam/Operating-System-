pages = [1, 2, 3, 4, 2, 3, 1]
frames = []
capacity = 3
fault = 0
hit = 0

for page in pages:
    if page not in frames:
        if len(frames) == capacity:
            frames.pop(0)

        frames.append(page)
        fault += 1
        result = "Fault"
    else:
        hit += 1
        result = "Hit"

    print(page, frames, result)

print("Total Hits:", hit)
print("Total Faults:", fault)
print("Hit Ratio:", hit / len(pages))
print("Fault Ratio:", fault / len(pages))