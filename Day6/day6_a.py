class Day:
    def __init__(self, startDay=0, daysUntilNewSpawn=0):
        self.daysUntilNewSpawn = daysUntilNewSpawn
        self.currentDay = startDay

    def newDay(self):
        self.currentDay = self.currentDay + 1
        self.daysUntilNewSpawn = self.daysUntilNewSpawn - 1
    
class Fish:
    def __init__(self, day):
        self.day = day
        
    def checkSpawn(self):
        fish = None
        if(self.day.daysUntilNewSpawn == 0):
            fish = Fish(Day(self.day.currentDay, 9))
            self.day.daysUntilNewSpawn = 7
        
        self.day.daysUntilNewSpawn = self.day.daysUntilNewSpawn - 1
        return fish

def main():
    with open('./testData') as f:
        content = f.readlines()
        days = [int(day) for day in content[0].split(',')]
        
    def newDay(fishes, currentDay):
        currentDay.newDay()
        for fish in fishes:
            newFish = fish.checkSpawn()
            if newFish != None:
                fishes.append(newFish)

    currentDay = Day()
    school = [Fish(Day(currentDay, day)) for day in days]

    for day in range(256):
        newDay(school, currentDay)
        print(day)

    print(len(school))
main()
