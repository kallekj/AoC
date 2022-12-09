import numpy as np


with open('./day-8/input') as f:
    allLines = f.readlines()
    forest = np.array([np.array(list(map(lambda x: int(x), np.array(
        list(line.rstrip('\n')))))) for line in allLines])


def isVisible(trees):
    highestTree = trees[0]  # First tree is always visible
    checkedTrees = [True]
    for tree in trees[1:]:  # Check all other trees
        if tree > highestTree:
            highestTree = tree
            checkedTrees.append(True)
        else:
            checkedTrees.append(False)
    return np.array(checkedTrees)


down = np.apply_along_axis(isVisible, 0, forest)
left = np.apply_along_axis(isVisible, 1, forest)
up = np.apply_along_axis(isVisible, 0, forest[::-1, :])[::-1, :]
right = np.apply_along_axis(isVisible, 1, forest[:, ::-1])[:, ::-1]

visibleTrees = up | down | left | right

print(visibleTrees.sum())
