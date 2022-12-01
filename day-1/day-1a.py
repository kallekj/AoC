from functools import reduce
import numpy as np

with open('./input') as f:
    data = "".join(f.readlines())


def adder(a, b):
    try:
        return int(a)+int(b)
    except Exception as e:
        print(e)
        return 0


allElvs = list(map(lambda elf: reduce(adder, list(map(lambda food: int(food), filter(lambda cal: cal != '', elf.split('\n'))))), data.split('\n\n')))

print(np.sum(sorted(allElvs)[-3:]))

