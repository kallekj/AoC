import numpy as np

with open('./testData') as f:
    content = f.readlines()
    data = np.array([line.split('\n')[0].split('|') for line in content])
    inData = [list(filter(None, line.split(' '))) for line in data[:,0]]
    outData = [list(filter(None, line.split(' ')))  for line in data[:,1]]
    

