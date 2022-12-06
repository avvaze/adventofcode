import re

partTwo = True

with open("in.txt", "r") as f:
    crates = [[] for _ in range(9)]
    while True:
        line = f.readline()
        if "1" in line: break

        for i in range(1, len(line), 4):
            if line[i] != " ": crates[i // 4].append(line[i])

    for a in crates: a.reverse()

    f.readline()

    while True:
        line = f.readline()
        if not line: break

        count, src, dst = map(int, re.sub(r"move | from | to ", " ", line).strip().split(" "))

        if partTwo:
            for i in range(count, 0, -1):
                crates[dst-1].append(crates[src-1].pop(-i))
        else: 
            for i in range(count):
                crates[dst-1].append(crates[src-1].pop())

    for stack in crates: print(stack)
    print("".join([a[-1] for a in crates if len(a) != 0]))
