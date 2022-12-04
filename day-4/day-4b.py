
def parsePair(pair):
    a, b = pair.split('-')
    return [int(a), int(b)]


with open('./input') as f:
    pairs = [ list(map(parsePair, line.rstrip('\n').split(','))) for line in f.readlines()]


def Intersection(a, b):
    aRange = range(a[0], a[1]+1)
    bRange = range(b[0], b[1]+1)
    return set(aRange).intersection(bRange)


counter = 0
for pair in pairs:
    if(len(Intersection(pair[0], pair[1])) > 0):
        counter += 1


print(counter)