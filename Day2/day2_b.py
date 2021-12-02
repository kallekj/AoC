class Submarine:
    def __init__(self):
        self.horizontalPos = 0
        self.depth = 0
        self.aim = 0

    def goForward(self, x):
        self.horizontalPos += x
        self.depth += self.aim * x

    def goDown(self, x):
        self.aim += x
    
    def goUp(self, x):
        self.aim -= x
    
    def multi(self):
        return self.depth * self.horizontalPos

    def getDepth(self):
        return self.depth
    
    def getHorizontalPos(self):
        return self.horizontalPos

def main():
    sub = Submarine()

    with open('./input') as f:
        content = f.readlines()
        lines = [ line.lstrip('\n') for line in content]
        
    
    for line in lines:
        if(line[0] == 'f'):
            sub.goForward(int(line[-2]))
        if(line[0] == 'd'):
            sub.goDown(int(line[-2]))
        if(line[0] == 'u'):
            sub.goUp(int(line[-2]))
    print(sub.multi())
    
main()

