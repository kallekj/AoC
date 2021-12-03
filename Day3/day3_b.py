import numpy as np

def getNewMatrixOxygen(theMatrix, i):
    retMatrix = []
    ones = np.sum(theMatrix.T[i])
    zeroes = len(theMatrix.T[i]) - np.sum(theMatrix.T[i])
    for j, firstRowVal in enumerate(theMatrix.T[i]):
        if(ones > theMatrix.shape[0]/2 and firstRowVal == 1):
            retMatrix.append(theMatrix[j])
        elif(zeroes > theMatrix.shape[0]/2 and firstRowVal == 0):
            retMatrix.append(theMatrix[j])
        elif(ones == zeroes and firstRowVal == 1):
            retMatrix.append(theMatrix[j])
    i += 1
    return (np.array(retMatrix), i)

def getNewMatrixCO2(theMatrix, i):
    retMatrix = []
    ones = np.sum(theMatrix.T[i])
    zeroes = len(theMatrix.T[i]) - np.sum(theMatrix.T[i])
    for j, firstRowVal in enumerate(theMatrix.T[i]):
        if(zeroes < theMatrix.shape[0]/2 and firstRowVal == 0):
            retMatrix.append(theMatrix[j])
        elif(ones < theMatrix.shape[0]/2 and firstRowVal == 1):
            retMatrix.append(theMatrix[j])
        elif(ones == zeroes and firstRowVal == 0):
            retMatrix.append(theMatrix[j])
    i += 1
    return (np.array(retMatrix), i)

with open('input') as f:
    content = f.readlines()
    matrix = np.array([ list(line.split('\n')[0]) for line in content])

matrixOxygen = matrix.astype(np.int64)
matrixCO2 = matrix.astype(np.int64)

i = 0
while (i < matrixOxygen.shape[1]):
    if( matrixOxygen.shape[0] == 1):
        break
    (matrixOxygen, i) = getNewMatrixOxygen(matrixOxygen, i)

i = 0
while (i < matrixCO2.shape[1]):
    if( matrixCO2.shape[0] == 1):
        break
    (matrixCO2, i) = getNewMatrixCO2(matrixCO2, i)

binStrOxygen = "".join([str(x) for x in matrixOxygen[0]])
binStrOxygenCO2 = "".join([str(x) for x in matrixCO2[0]])

oxygen = int(binStrOxygen, 2)
co2 = int(binStrOxygenCO2, 2)

print(oxygen*co2)




