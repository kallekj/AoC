import numpy as np

with open('./input') as f:
    content = f.readlines()
    horizontalPosition = np.array([int(position) for position in content[0].split(',')])

maxPos = np.max(horizontalPosition)
minPos = np.min(horizontalPosition)

fuelArr = []
for pos in range(minPos, maxPos + 1):
    posArr = np.array([pos]*len(horizontalPosition))
    dists = np.abs(horizontalPosition - pos)
    fuel = np.array([np.sum(np.arange(dist + 1)) for dist in dists])
    fuelArr.append(np.sum(fuel))
    print("{}/{}".format(pos, maxPos))

print(np.min(fuelArr))