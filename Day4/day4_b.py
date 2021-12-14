import numpy as np

class Number:
    def __init__(self, val):
        self.val = val
        self.visited = False
    
    def isVisited(self):
        return self.visited == True
    

class Board:
    
    def __init__(self, matrix):
        def initMatrix(matrix):
            flattenMatrix = matrix.flatten()
            numArray = np.array([ Number(int(val)) for val in flattenMatrix])
            numMatrix = numArray.reshape((5,5))
            return numMatrix

        self.matrix = initMatrix(matrix)
        self.bingo = False

    def markNumber(self, val):
        flattenMatrix = self.matrix.flatten()
        for num in flattenMatrix:
            if num.val == val:
                num.visited = True

        flattenMatrix = flattenMatrix.reshape((5,5))
    
    def checkRow(self):
        for row in self.matrix:
            s = 0
            for num in row:
                if num.isVisited():
                    s += 1
                if s == 5:
                    self.bingo = True
                    return True
        return False
    
    def checkCol(self):
        for col in self.matrix.T:
            s = 0
            for num in col:
                if num.isVisited():
                    s += 1
                if s == 5:
                    self.bingo = True
                    return True
        return False
    
    def countUnMarked(self):
        s = 0
        for row in self.matrix:
            for num in row:
                if num.isVisited() == False:
                    s += num.val
        return s

def parseMatrix(board):
    board = board.split('\n')
    matrix = np.array([list(filter(None, row.split(' '))) for row in board])
    return matrix

def countBingo(boards):
    count = 0
    for board in boards:
        if board.bingo:
            count += 1
    return count

def solve(randomNumbers, boards):
    for val in randomNumbers:
        for board in boards:
            board.markNumber(val)
            board.checkRow()
            board.checkCol()
            if countBingo(boards) == len(boards):
                return board.countUnMarked() * val
                
    return None

def main():
    with open('./input') as f:
        content = f.readlines()
        randomNumbers = content[0].split('\n')[0]
        randomNumbers = [int(x) for x in "".join(randomNumbers).split(',')]

        boards = "".join(content[2:]).split('\n\n')
        boards = [ Board(parseMatrix(board)) for board in boards]


    print(solve(randomNumbers, boards))


    
    
main()
