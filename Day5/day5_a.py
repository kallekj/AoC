import re
import numpy as np

class OceanFloorPos:
    def __init__(self, x, y):
        self.vents = 1
        self.pos = [x, y]
    
class OceanFloor:
    def __init__(self):
        self.visitedPositions = []
        self.map = []


    def addVents(self, a, b):
        (x1,y1) = a
        (x2,y2) = b

        if x1 == x2:
            Ymax = max([y1, y2])
            Ymin = min([y1, y2])
            positions = [[x1, y] for y in range(Ymin, Ymax)]

        if y1 == y2:
            Xmax = max([x1, x2])
            Xmin = min([x1, x2])
            positions = [[x, y1] for x in range(Xmin, Xmax)]

        if len(self.map) == 0:
            for pos in positions:
                floorPos = OceanFloorPos(pos[0], pos[1])
                self.map.append(floorPos)
                self.visitedPositions.append(floorPos.pos) 

        else:
            for pos in positions:
                if pos in self.visitedPositions:
                    temp = np.array(self.visitedPositions)
                    index = np.where(x==pos)
                    print(index)
                    self.map[index].vents += 1
                else:
                    floorPos = OceanFloorPos(pos[0], pos[1])
                    self.map.append(floorPos)
                    self.visitedPositions.append(floorPos.pos)

        # if len(self.map) == 0:
        #     for pos in positions:
        #         floorPos = OceanFloorPos(pos[0], pos[1])
        #         self.map.append(floorPos)
        # else:
        #     for i, pos in enumerate(positions):
        #         for vent in self.map:
        #             if vent.pos == pos:
        #                 vent.vents += 1
        #                 positions.pop(i)

        #     for pos in positions:
        #         floorPos = OceanFloorPos(pos[0], pos[1])
        #         self.map.append(floorPos)
    
    def countDangerousPositions(self):
        numDangerousPositions = 0
        for pos in self.map:
            if pos.vents >= 2:
                numDangerousPositions += 1
        return numDangerousPositions

def main():
    oceanFloor = OceanFloor()

    with open('./testData') as f:
        content = f.readlines()
        tot = len(content)
        for i, line in enumerate(content):
            line = list(filter(None, re.split('[^\d]', line)))
            x1 = int(line[0])
            y1 = int(line[1])
            x2 = int(line[2])
            y2 = int(line[3])
            print("{}%".format(round(i/tot, 2)*100))
            oceanFloor.addVents((x1,y2), (x2,y2))

    print(oceanFloor.countDangerousPositions())

main()



    