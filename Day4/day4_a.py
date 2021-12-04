import numpy as np

class Number:
    def __init__(self, val):
        self.val = val
        self.visited = 0
    
    def visited(self):
        self.visited = 1
    
    def isVisited(self):
        return self.visited == 1
    

class Board:
    
    def __init__(self, matrix):
        def initMatrix(matrix):
            flattenMatrix = matrix.flatten()
            numArray = np.array([ Number(val) for val in flattenMatrix])
            numMatrix = numArray.reshape((5,5))
            return numMatrix

        self.matrix = initMatrix(matrix)

    def markNumber(self, val):
        flattenMatrix = self.matrix.flatten()
        for num in flattenMatrix:
            if num.val == val:
                num.visited()
        flattenMatrix = flattenMatrix.reshape((5,5))


def main():
    with open('./input') as f:
        content = f.readlines()
        for line in content:
            if(len(line) > 7):
                randomNumbers = list(line.split('\n')[0])
        matrix = np.array([ list(line.split('\n')[0]) for line in content])
    
    
