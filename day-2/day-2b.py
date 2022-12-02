
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

rock = ['A']
paper = ['B']
scissors = ['C']
rulesWin = {
    "A": "B",
    "B": "C",
    "C": "A"
}
rulesLoss = {
    "A": "C",
    "B": "A",
    "C": "B"
}

with open('./test') as f:
    rounds = [ line.rstrip('\n').split(' ') for line in f.readlines()]

def handValue(hand):
    if hand in rock:
        return 1
    elif hand in paper:
        return 2
    else:
        return 3

def calcScore(round, result):
    if(result == 'draw'):
        return 3 + handValue(round[0])
    elif(result == 'loss'):
        return 0 + handValue(rulesLoss[round[0]])
    else:
        return 6 + handValue(rulesWin[round[0]])

score = 0
for round in rounds:
    if(round[1] == 'Y'):
        score += calcScore(round, 'draw')
    elif(round[1] == 'X'):
        score += calcScore(round, 'loss')
    else:
        score += calcScore(round, 'win')

print(score)
