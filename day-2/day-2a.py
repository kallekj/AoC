
# A, X = Rock = 1
# B, Y = Paper = 2
# C, Z = Scissors = 3
# Loss = 0
# Win = 6
# Rock VS Scissors = Rock
# Rock VS Paper = Paper
# Rock VS Rock = Draw
# Scissors VS Paper = Scissors
# Scissors VS Scissors = Draw
# Paper VS Paper = Draw

rock = ['A', 'X']
paper = ['B', 'Y']
scissors = ['C', 'Z']
rules = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

with open('./input') as f:
    rounds = [ line.rstrip('\n').split(' ') for line in f.readlines()]

def handValue(hand):
    if hand in rock:
        return 1
    elif hand in paper:
        return 2
    else:
        return 3

def whoWins(round, roundWonBy):
    if(roundWonBy == 'draw'):
        return 3 + handValue(round[1])
    elif(round[0] in rules[roundWonBy]):
        return 0 + handValue(round[1])
    else:
        return 6 + handValue(round[1])

score = 0
for round in rounds:
    if(handValue(round[0]) == handValue(round[1])):
        print(whoWins(round, 'draw'))
        score += whoWins(round, 'draw')
    elif all(i in rock + scissors for i in round) and not all(i in paper for i in round): # Rock wins
        print(whoWins(round, 'rock'))
        score += whoWins(round, 'rock')
    elif all(i in rock + paper for i in round) and not all(i in scissors for i in round): # Paper wins
        print(whoWins(round, 'paper'))
        score += whoWins(round, 'paper')
    elif all(i in scissors + paper for i in round) and not all(i in rock for i in round): # scissors wins
        print(whoWins(round, 'scissors'))
        score += whoWins(round, 'scissors')
    
        

print(score)
