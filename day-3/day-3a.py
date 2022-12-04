
with open('./input') as f:
    bags = [ line.rstrip('\n') for line in f.readlines()]


commonChars = []

for bag in bags:
    bagA = bag[:len(bag)//2]
    bagB = list(bag[len(bag)//2:])
    for item in bagA:
        if item in bagB:
            asciiValue = ord(item)
            if asciiValue >= 65 and asciiValue <= 90:
                commonChars.append(asciiValue - 38) # A = 27, B = 28 ...
            else:
                commonChars.append(asciiValue - 96)
            break
    


print(sum(commonChars))