const fs = require('fs');

function move_score(move) {
    switch(move) {
        case "rock": return 1;
        case "paper": return 2;
        case "scissors": return 3;
    }
}

function map_code_to_move(code) {
    switch (code) {
        case 'A':
        case 'X':
            return "rock";
        case 'B':
        case 'Y':
            return "paper";
        case 'C':
        case 'Z':
            return "scissors";
    }
}

function losing_move_against(move) {
    switch (move) {
        case "rock": return "scissors";
        case "paper": return "rock";
        case "scissors": return "paper";
    }
}

function winning_move_against(move){
    return losing_move_against(losing_move_against(move));
}

function round_result(move1, move2){
    if (move1 == move2) return 3; // both moves are the same, it's a draw
    if (move2 == losing_move_against(move1)) return 0; // move1 (their move) wins
    return 6; // move 2 (our move) wins
}


const input = fs.readFileSync('in.txt', "utf-8").split("\r\n");


let score = 0;

for (const line of input) {

    const [their_move, our_move] = line.split(" ").map(map_code_to_move);
    
    score += move_score(our_move);
    score += round_result(their_move, our_move);
}
console.log(`Puzzle 1 answer: ${score}`);



// ####################
// Puzzle 2
// ####################

function result_to_move(result, move1) {
    switch (result) {
        case 'Y': return move1;
        case 'X': return losing_move_against(move1);
        case 'Z': return winning_move_against(move1);
    }
}


score = 0;
for (const line of input) {
    let [their_move, desired_result] = line.split(" ");
    their_move = map_code_to_move(their_move);

    const our_move = result_to_move(desired_result, their_move);

    score += move_score(our_move);
    score += round_result(their_move, our_move);

}

console.log(`Puzzle 2 answer: ${score}`);