import re

with open('./input') as f:
    content = [line.rstrip('\n') for line in f.readlines()]

creates = {}
numCreates = 9
for i in range(numCreates):
    creates[i] = []

def addCreate(char, pos):
    if(char != ' '):
        creates[pos].insert(0, char)


def moveCreate(src, dst, num):
    tempList = creates[int(src)-1][len(creates[int(src)-1])-int(num):]
    creates[int(dst)-1].extend(tempList)
    del creates[int(src)-1][len(creates[int(src)-1])-int(num):]


def printTopCases():
    output = ""
    for case in creates:
        output += creates[case][-1]
    print(output)


for line in content:
    if len(line) > 0 and line[1] not in ['1', 'o']:
        for i in range(0, numCreates):
            addCreate(line[i*4+1], i)
    elif len(line) > 0 and line[1] != '1':
        moves = re.findall(r'[0-9]{2}|[0-9]{1}', line)
        moveCreate(moves[1], moves[2], moves[0])
    else:
        continue


printTopCases()
