import numpy as np

with open('./input') as f:
    content = f.readlines()

noNewLines = np.array([line.lstrip('\n') for line in content])
