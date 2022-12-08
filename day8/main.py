import functools


with open("in.txt") as f:
    data = [list(map(int, [*line])) for line in f.read().splitlines()]

    width = len(data[0])
    height = len(data)

    count = 2*width + 2*height - 4

    for i in range(1, height-1):
        for j in range(1, width-1):

            h = data[i][j]

            left = data[i][:j]
            right = data[i][j+1:]
            up = [line[j] for line in data[:i]]
            down = [line[j] for line in data[i+1:]]

            # Part 1 
            if (h>max(left) or h>max(right) or h>max(up) or h>max(down)):
                count += 1

    print("Solution:", count)


    # Part 2
    max_score = 0    
    for i in range(1, height-1):
        for j in range(1, width-1):

            h = data[i][j]

            dirs = [
                data[i][j-1::-1],
                data[i][j+1:],
                [line[j] for line in data[i-1::-1]],
                [line[j] for line in data[i+1:]]
            ]

            scores = [0,0,0,0]
            for d in range(4):
                for tree in dirs[d]:
                    scores[d] += 1
                    if tree >= h:
                        break

            view_score = functools.reduce(lambda a, b: a*b, scores)
            if view_score > max_score:
                max_score = view_score

    print("Solution 2:", max_score)