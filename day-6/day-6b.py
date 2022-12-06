windowSize = 14

with open('./input') as f:
    datastream = [ list(line.rstrip('\n')) for line in f.readlines()][0]

def checkStartCode(sublist):
    if len(set(sublist)) == windowSize:
        return True
    else:
        return False

for i in range(len(datastream) - windowSize + 1):
    if checkStartCode(datastream[i:i+windowSize]):
        print(i+windowSize)
        break
