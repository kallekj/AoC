
with open('./input') as f:
    content = f.readlines()

noNewLines = [int(line.lstrip('\n')) for line in content]

prev = 0
indexLow = 0
indexHigh = 3
count = 0
for i in range(len(noNewLines)):
    if(indexHigh > len(noNewLines) + 1):
        break
    if prev == 0:
        prev = sum(noNewLines[indexLow:indexHigh])
        indexLow += 1
        indexHigh += 1
        continue
    if prev < sum(noNewLines[indexLow:indexHigh]):
        count += 1
    prev = sum(noNewLines[indexLow:indexHigh])
    indexLow += 1
    indexHigh += 1
print(count)