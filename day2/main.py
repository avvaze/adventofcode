
def move_score(move):
    match(move):
        case "rock": return 1
        case "paper": return 2
        case "scissors": return 3

def map_code_to_move(code):
    match (code):
        case 'A' | 'X': return "rock"
        case 'B' | 'Y': return "paper"
        case 'C' | 'Z': return "scissors"

def losing_move_against(move):
    match (move):
        case "rock": return "scissors"
        case "paper": return "rock"
        case "scissors": return "paper"

def winning_move_against(move):
    match (move):
        case "rock": return "paper"
        case "paper": return "scissors"
        case "scissors": return "rock"

def round_result(move1, move2):
    if move1 == move2: return 3
    if move2 == losing_move_against(move1): return 0
    return 6


with open("in.txt", "r") as f:

    score = 0

    for line in f:
        their_move, our_move = tuple(map(lambda m: map_code_to_move(m), line.strip().split(" ")))
        
        score += move_score(our_move)
        score += round_result(their_move, our_move)

    print(f"Puzzle 1 Score: {score}")


def result_to_move(result, move1):
    match(result):
        case 'Y': return move1
        case 'X': return losing_move_against(move1)
        case 'Z': return winning_move_against(move1)


with open("in.txt", "r") as f:

    score = 0
    
    for line in f:
        their_move, desired_result = tuple(line.strip().split(" "))
        their_move = map_code_to_move(their_move)

        our_move = result_to_move(desired_result, their_move)

        score += move_score(our_move)
        score += round_result(their_move, our_move)

    print(f"Puzzle 2 score: {score}")