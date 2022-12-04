
with open('./input') as f:
    bags = [ line.rstrip('\n') for line in f.readlines()]


commonChars = []

for i in range(0, len(bags), 3):
    for item in bags[i]:
        if item in list(bags[i+1]) and item in list(bags[i+2]):
            asciiValue = ord(item)
            if asciiValue >= 65 and asciiValue <= 90:
                commonChars.append(asciiValue - 38) # A = 27, B = 28 ...
            else:
                commonChars.append(asciiValue - 96)
            break
    


print(sum(commonChars))