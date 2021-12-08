from collections import deque

def main(): 
    with open('./input') as f:
        content = f.readlines()
        days = [int(day) for day in content[0].split(',')]
    
    school = deque([0,0,0,0,0,0,0,0,0])
    for day in days:
        school[day] += 1

    for day in range(1, 257):  
        numNewFish = school[0]
        school.rotate(-1)
        school[6] += numNewFish
        
        print("After day: {}    Fishes: {}".format(day, sum(school)))
    
    print(sum(school))
    #print(len(school))
main()
