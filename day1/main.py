
with open("in.txt", "r") as f:
    max_cals = 0
    calories = 0
    while True:
        line = f.readline()
        if not line:
            break
        if (line == "\n"):
            calories = 0
        else:
            calories += int(line.strip())
            if calories > max_cals:
                max_cals = calories

    print(max_cals)


# Problem 2
with open("in.txt", "r") as f:
    i = 0
    calorie_list = [0]
    while True:
        line = f.readline()
        if not line:
            break
        if (line == "\n"):
            i += 1
            calorie_list.append(0)
        else:
            calorie_list[i] += int(line.strip())

    # sort the list
    calorie_list.sort()
    top_three = calorie_list[-3:]
    print(top_three, sum(top_three))
        

    print(max_cals)