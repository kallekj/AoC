import numpy as np

with open('./input') as f:
    content = f.readlines()
    matrix = np.array([ list(line.split('\n')[0]) for line in content])

matrix = matrix.astype(np.int64)
colSums = np.sum(matrix, axis=0)
gammaBin = []
for col in colSums:
    if col > matrix.shape[0]/2:
        gammaBin.append("1")
    else:
        gammaBin.append("0")

epsilonBin = "".join([ "1" if x != "1" else "0" for x in gammaBin])
gammaBin = "".join(gammaBin)
epsilon = int(epsilonBin, 2)
gamma = int(gammaBin, 2)

print(epsilon * gamma)


