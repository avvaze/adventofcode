
dirs = {
}
current_dir = []

# Create a dict of all dirs and files
with open("in.txt", "r") as f:
    for line in f:

        if line.startswith("$ ls"):
            continue
        if line.startswith("$ cd .."):
            current_dir.pop()
            continue
        
        if line.startswith("$ cd"):
            current_dir.append(line[4:].strip())
            id = "-".join(current_dir)
            if id not in dirs:
                dirs[id] = {
                    "dirs": [],
                    "files": []
                }
            continue

        a, b = line.strip().split(" ")
        id = "-".join(current_dir)
        if a == "dir":
            dirs[id]["dirs"].append(b)
        else:
            dirs[id]["files"].append(int(a))


def dir_size(dir):
    return sum(dirs[dir]["files"] + [dir_size(f"{dir}-{d}") for d in dirs[dir]["dirs"]])

print("Solution 1:", sum(filter(lambda s: s <= 100000, [dir_size(dir) for dir in dirs])))


dir_sizes = {
}

while len(dir_sizes) != len(dirs):
    for dir in dirs:
        if dir in dir_sizes:
            continue

        size = 0
        failed = False
        for sub_dir in dirs[dir]["dirs"]:
            if (dir + "-" + sub_dir) in dir_sizes:
                size += dir_sizes[dir + "-" + sub_dir]
            else:
                failed = True
                break

        if not failed:
            for file in dirs[dir]["files"]:
                size += file
            dir_sizes[dir] = size

print("Solution 2:", sum([ s for s in dir_sizes.values() if s <= 100000]))

# Part 2
min_space_needed = dir_sizes["/"] - (70_000_000 - 30_000_000)
print("Size of dir to delete:", min([s for s in dir_sizes.values() if s >= min_space_needed]))


