scores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("in.txt", "r") as f:
    score = 0
    for rs in f:
        size = len(rs)
        c1 = rs[:size//2]
        c2 = rs[size//2:]
        for item in c2:
            if (item in c1):
                score += scores.index(item) +1
                break

    print(score)


with open("in.txt", "r") as f:
    input = f.read().splitlines()
    score = 0
    for i in range(0, len(input), 3):
        r1, r2, r3 = input[i:i+3]
        for item in r1:
            if (item in r2 and item in r3):
                score += scores.index(item) +1
                break

    print(score)