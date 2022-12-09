const fs = require("fs");

// Read the file
const f = fs.readFileSync("in.txt", "utf-8");

// This is gonna contain an entry for every directory in the file system
// example:
// {
//     "/": {
//         "dirs": ["dir1", "dir2"],    // all sub directories
//         "files": [100, 200]          // all files in this directory (only size needed)
//     },
//     "/-dir1": {                      // sub directories are separated with dashes, so everyone can
//         "dirs": ["dir3"],            // have a unique id (some folders have the same name)
//         "files": [300]
//     },
// }
const dirs = {};

// This is gonna contain the current directory
// example: ["/", "dir1"] means we are in /-dir1
const current_dir = [];


// Create a dict of all dirs and files
for (const line of f.split("\r\n")) {

    // We dont care about ls, because we can identifiy the output of ls
    // by the fact that it doesnt start with a $
    if (line.startsWith("$ ls"))
        continue;
    
    // If we cd .., we go one directory up, aka we remove the last item from current_dir
    if (line.startsWith("$ cd ..")) {
        current_dir.pop();
        continue;
    }
    
    // If we cd into a directory, we add it to current_dir
    // then we check if we already have an entry for this directory in "dirs", if not we create one
    if (line.startsWith("$ cd")) {

        current_dir.push(line.slice(4).trim())

        const id = current_dir.join("-");

        // If we dont have an entry for this directory, create one
        if (!(id in dirs)) {
            dirs[id] = {
                dirs: [],
                files: []
            }
            continue;
        }
    }

    // If we are here, it means the line is part of the output of ls
    // now we need to check if it is a directory or a file, then
    // we add it into "dirs" with the correct id
    const [a, b] = line.trim().split(" ");
    const id = current_dir.join("-");

    // If it is a directory, we add it to dirs
    if (a == "dir")
        dirs[id].dirs.push(b)
    // If it is a file, we add it to files
    else
        dirs[id].files.push(Number(a))
}

// Now we can write a recursive function to calculate the size of a directory
// For any directory we want to know the size of, we just have to sum um all files in that directory,
// and then call the function for every sub directory and add the result to the sum
function dir_size(dir) {
    let size = dirs[dir].files.reduce((a, b) => a + b, 0);
    for (const sub_dir of dirs[dir].dirs) {
        size += dir_size(dir + "-" + sub_dir);
    }
    return size;
}

const solution = Object.keys(dirs).map(dir_size).filter(s => s <= 100000).reduce((a, b) => a + b, 0);
console.log("Solution 1:", solution);