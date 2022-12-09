import numpy as np


with open('./day-8/input') as f:
    allLines = f.readlines()
    forest = np.array([np.array(list(map(lambda x: int(x), np.array(
        list(line.rstrip('\n')))))) for line in allLines])


def calc_viewing_distance(treePos):
    treeHeight = forest[treePos]
    distances = []
    sight = 0
    
    # left from tree
    for y in range(treePos[1]-1, - 1, -1):
        sight += 1
        if treeHeight <= forest[treePos[0], y]:
            break
    
    if sight > 0:
        distances.append(sight)
    
    sight = 0

    # right from tree
    for y in range(treePos[1]+1, forest.shape[1], 1):
        sight += 1
        if treeHeight <= forest[treePos[0], y]:
            break

    if sight > 0:
        distances.append(sight)
    
    sight = 0

    # up from tree
    for x in range(treePos[0]-1, -1, -1):
        sight += 1
        if treeHeight <= forest[x, treePos[1]]:
            break

    if sight > 0:
        distances.append(sight)
    
    sight = 0

    # down from tree
    for x in range(treePos[0]+1, forest.shape[0], 1):
        sight += 1
        if treeHeight <= forest[x, treePos[1]]:
            break

    if sight > 0:
        distances.append(sight)

    return np.prod(distances)
    

print(np.max([calc_viewing_distance(tree) for tree in zip(*np.nonzero(forest))]))
