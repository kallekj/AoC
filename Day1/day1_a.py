
with open('./input') as f:
    content = f.readlines()

noNewLines = [line.lstrip('\n') for line in content]

prev = 0
count = 0
for line in noNewLines:
    if prev == 0:
        prev = prev = int(line)
        continue
    if prev < int(line):
        count += 1
    prev = int(line)
print(count)