class Node:

    def __init__(self, pos, parent, cost, depth):
        self.pos = pos
        self.parent = parent
        self.cost = cost
        self.depth = depth

    def set_parent(self, newParent):
        self.parent = newParent

    def set_cost(self, newCost):
        self.cost = newCost

    def __hash__(self) -> int:
        return hash(str(self.pos))

    def __eq__(self, __o: object) -> bool:
        if type(__o) == list:
            return hash(str(__o)) == hash(str(self.pos))
        else:
            return hash(__o) == hash(self)

    def __lt__(self, __o: object) -> bool:
        return self.cost < __o.cost

    def __gt__(self, __o: object) -> bool:
        return self.cost > __o.cost

    def __str__(self) -> str:
        return f'[{self.pos[0]}, {self.pos[1]}] c: {self.cost}'
