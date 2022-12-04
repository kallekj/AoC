
def parsePair(pair):
    a, b = pair.split('-')
    return [int(a), int(b)]


with open('./input') as f:
    pairs = [ list(map(parsePair, line.rstrip('\n').split(','))) for line in f.readlines()]


def checkSubset(a, b):
    aRange = range(a[0], a[1]+1)
    bRange = range(b[0], b[1]+1)
    if(all(x in aRange for x in bRange)):
        return True
    else:
        return False


counter = 0
for pair in pairs:
    if(checkSubset(pair[0], pair[1]) or checkSubset(pair[1], pair[0])):
        counter += 1


print(counter)