const fs = require('fs');

const scores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

const input = fs.readFileSync('in.txt', "utf-8").split("\r\n");

let score = 0;
for (const rs of input) {
    const size = rs.length;
    const c1 = rs.slice(0, size / 2);
    const c2 = rs.slice(size / 2);

    for (const item of c2) {
        if (c1.includes(item)) {
            score += scores.indexOf(item) +1
            break
        }
    }
}

console.log(score)


score = 0
for (let i = 0; i < input.length; i+=3) {
    const [r1, r2, r3] = input.slice(i, i+3);
    for (const item of r1) {
        if (r2.includes(item) && r3.includes(item)) {
            score += scores.indexOf(item) +1
            break
        }
    }
}
console.log(score)