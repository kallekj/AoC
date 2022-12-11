import numpy as np
import pandas as pd
import os
def clear(): return os.system('clear')


shouldPrint = False


class Knot:

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y
        self.visitedPositions = set()
        self.visitedPositions.add((0, 0))
        self.previousPosition = (x, y)

    def visitNode(self, node):
        self.previousPosition = (self.x, self.y)
        self.x = node[0]
        self.y = node[1]
        self.visitedPositions.add(node)

    def getCurrentNode(self):
        return (self.x, self.y)

    def getPreviousNode(self):
        return self.previousPosition

    def getVisitedPositions(self):
        return len(self.visitedPositions)


#start = (11, 5)
start = (0, 0)
head = Knot(*start)
knots = [Knot(*start) for _ in range(8)]
tail = Knot(*start)


def moveHead(direction):
    match direction:
        case 'U':
            currentNode = head.getCurrentNode()
            head.visitNode((currentNode[0], currentNode[1] + 1))
        case 'D':
            currentNode = head.getCurrentNode()
            head.visitNode((currentNode[0], currentNode[1] - 1))
        case 'L':
            currentNode = head.getCurrentNode()
            head.visitNode((currentNode[0] - 1, currentNode[1]))
        case 'R':
            currentNode = head.getCurrentNode()
            head.visitNode((currentNode[0] + 1, currentNode[1]))


def moveKnot(knot: Knot, prevKnot: Knot):
    thisKnotPosition = np.array(knot.getCurrentNode())
    previousKnotPosition = np.array(prevKnot.getCurrentNode())
    itShouldMove = np.max(np.abs(thisKnotPosition - previousKnotPosition)) > 1
    if itShouldMove:
        x, y = previousKnotPosition - thisKnotPosition
        x = thisKnotPosition[0] + np.clip(x, -1, 1)
        y = thisKnotPosition[1] + np.clip(y, -1, 1)
        knot.visitNode((x, y))


if shouldPrint:
    matrix = np.array([['.']*21]*26)
    #matrix = np.array([['.']*5]*6)
    df = pd.DataFrame(matrix)
    df.rename_axis(None, axis=1, inplace=True)
    df.rename_axis(None, axis=0, inplace=True)
    df.loc[start] = 'S'
    print(df.to_string(index=False, header=False))


def updateMap(knot: Knot, marker):
    if shouldPrint:
        df.loc[knot.getCurrentNode()] = marker
        df.loc[knot.getPreviousNode()] = '.'
        clear()
        print(df.to_string(index=False, header=False))


def move(instruction):
    direction, steps = instruction.split(' ')
    for _ in range(int(steps)):
        moveHead(direction)
        updateMap(head, 'H')

        for i, knot in enumerate(knots):
            if i == 0:  # previous is head
                moveKnot(knot, head)
            else:
                moveKnot(knot, knots[i-1])
            updateMap(knot, str(i+1))

        moveKnot(tail, knots[-1])  # Last knot
        updateMap(knot, str(9))


with open('./day-9/input') as f:
    instructions = [line.rsplit('\n') for line in f.readlines()]


for instruction in instructions:
    move(instruction[0])


if shouldPrint:
    for pos in tail.visitedPositions:
        if pos == start:
            df.loc[pos] = 'S'
        else:
            df.loc[pos] = '#'


print(tail.getVisitedPositions())

if shouldPrint:
    print(df.to_string(index=False, header=False))
