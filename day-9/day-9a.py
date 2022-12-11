
class RopeEnd:

    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.visitedPositions = set()
        self.visitedPositions.add((0,0))
        self.previousPosition = None

    def visitNode(self, node):
        self.previousPosition = (self.x, self.y)
        self.x = node[0]
        self.y = node[1]
        self.visitedPositions.add(node)

    def getCurrentNode(self):
        return (self.x, self.y)
    
    def getPreviousNode(self):
        return self.previousPosition

    def getVisitedPositions(self):
        return len(self.visitedPositions)


head = RopeEnd()
tail = RopeEnd()

def moveHead(direction):
    match direction:
        case 'U':
            currentNode = head.getCurrentNode()
            head.visitNode((currentNode[0], currentNode[1] + 1))
        case 'D':
            currentNode = head.getCurrentNode()
            head.visitNode((currentNode[0], currentNode[1] - 1))
        case 'L':
            currentNode = head.getCurrentNode()
            head.visitNode((currentNode[0] - 1, currentNode[1]))
        case 'R':
            currentNode = head.getCurrentNode()
            head.visitNode((currentNode[0] + 1, currentNode[1]))


def headNotInDiagFromTail():
    currentNode = tail.getCurrentNode()
    #upper right
    ur =  (currentNode[0]-1, currentNode[1]+1)
    if head.getCurrentNode() == ur: return False
    #upper left
    ul = (currentNode[0]+1, currentNode[1]+1)
    if head.getCurrentNode() == ul: return False
    #lower left
    ll = (currentNode[0]+1, currentNode[1]-1)
    if head.getCurrentNode() == ll: return False
    #lower right
    lr = (currentNode[0]-1, currentNode[1]-1)
    if head.getCurrentNode() == lr: return False

    return True


def headNotInContactWithTail():
    currentNode = tail.getCurrentNode()
    #upper
    u =  (currentNode[0], currentNode[1]+1)
    if head.getCurrentNode() == u: return False
    #left
    l = (currentNode[0]+1, currentNode[1])
    if head.getCurrentNode() == l: return False
    #under
    d = (currentNode[0], currentNode[1]-1)
    if head.getCurrentNode() == d: return False
    #right
    r = (currentNode[0]-1, currentNode[1])
    if head.getCurrentNode() == r: return False

    return True


def moveTail(direction):
    match direction:
        case 'U':
            currentHeadNode = head.getCurrentNode()
            nextTailNode = (currentHeadNode[0], currentHeadNode[1] - 1)
            if headNotInDiagFromTail() and currentHeadNode != tail.getCurrentNode() and headNotInContactWithTail():
                tail.visitNode(nextTailNode)
        case 'D':
            currentHeadNode = head.getCurrentNode()
            nextTailNode = (currentHeadNode[0], currentHeadNode[1] + 1)
            if headNotInDiagFromTail() and currentHeadNode != tail.getCurrentNode() and headNotInContactWithTail():
                tail.visitNode(nextTailNode)
        case 'L':
            currentHeadNode = head.getCurrentNode()
            nextTailNode = (currentHeadNode[0] + 1, currentHeadNode[1])
            if headNotInDiagFromTail() and currentHeadNode != tail.getCurrentNode() and headNotInContactWithTail():
                tail.visitNode(nextTailNode)
        case 'R':
            currentHeadNode = head.getCurrentNode()
            nextTailNode = (currentHeadNode[0] - 1, currentHeadNode[1])
            if headNotInDiagFromTail() and currentHeadNode != tail.getCurrentNode() and headNotInContactWithTail():
                tail.visitNode(nextTailNode)


def move(instruction):
    direction, steps = instruction.split(' ')
    for _ in range(int(steps)):
        moveHead(direction)
        moveTail(direction)

with open('./day-9/input') as f:
    instructions = [line.rsplit('\n') for line in f.readlines()]


for instruction in instructions:
    move(instruction[0])


print(tail.getVisitedPositions())
