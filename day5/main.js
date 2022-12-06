// AoC 2022 Day 5

const fs = require('fs');

const input = fs.readFileSync('in.txt', "utf-8").split("\r\n");

// Index of empty line in input so we can split the stack definition from the instructions
const idx = input.indexOf("");

const stackDef = input.slice(0, idx-1);
const instructions = input.slice(idx + 1);


const crates = [ [], [], [], [], [], [], [], [], [] ];

for (const line of stackDef) {
    for (let i = 0; i < 9; i++) {
        const crate = line[1 + i*4];
		// If there is a crate, push it onto its stack
        if (crate !== " ") crates[i].push(crate)
    }
}

// We pushed the crates on the stacks in reverse order, so we need to reverse them
crates.forEach(a => a.reverse());


for (const line of instructions) {
    const [count, src, dst] = line
        .replace(/move | from | to /gi, " ") // turn "move 3 from 1 to 2" into "3 1 2"
        .trim()                                                 // remove leading and trailing whitespace
        .split(" ")                                     // turn "3 1 2" into ["3", "1", "2"]
        .map(Number);                                           // turn ["3", "1", "2"] into [3, 1, 2]
    
    const partOne = true;
    if (partOne){
        // Slice the last <count> items from the source stack and push them onto the destination stack
        // Since every create is pushed over one at a time, we need to reverse the order of the crates
        crates[dst-1] = crates[dst-1].concat(crates[src-1].splice(-count).reverse());
    } else {
        // Do the same as above, but don't reverse the order of the crates,
        // as they arent moved one at a time
        crates[dst-1] = crates[dst-1].concat(crates[src-1].splice(-count));
    }
}

// print the stacks (for debugging)
for (const stack of crates) console.log(stack);

// grab the topmost item from every stack and join them together
console.log(crates.map(a => a.slice(-1)).join(""))
