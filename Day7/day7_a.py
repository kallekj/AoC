import numpy as np

with open('./input') as f:
    content = f.readlines()
    horizontalPosition = np.array([int(position) for position in content[0].split(',')])

maxPos = np.max(horizontalPosition)
minPos = np.min(horizontalPosition)

fuelArr = []
for pos in range(minPos, maxPos + 1):
    posArr = np.array([pos]*len(horizontalPosition))
    fuel = np.sum(np.abs(horizontalPosition - pos))
    fuelArr.append(fuel)
    print("{}/{}".format(pos, maxPos))

print(np.min(fuelArr))