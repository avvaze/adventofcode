import re

with open("in.txt", "r") as f:

    count = 0

    for pair in f:
        a0, a1, b0, b1 = map(int, re.split(r",|-", pair))

        if (a0 >= b0 and a1 <= b1) or (a0 <= b0 and a1 >= b1):
            count += 1

    print(count)


with open("in.txt", "r") as f:

    count = 0
    c2 = 0

    for pair in f:
        c2 += 1
        a0, a1, b0, b1 = map(int, re.split(r",|-", pair))

        if (b0 <= a1 and b1 >= a0) or (a0 <= b1 and a1 >= b0):
            count += 0
        if (a0 <= b0 <= a1) or (b0 <= a0 <= b1):
            count += 1

    print(count, c2)