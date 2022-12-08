const fs = require('fs');

const data = fs.readFileSync("in.txt", "utf8");
const mlen = 14; // Length of the marker

for (let i = 0;; i++) {

    const chars = data.slice(i, i + mlen);

    if (new Set(chars).size == mlen) {
        console.log(`First marker after ${i + mlen} characters`);
        break;
    }
}