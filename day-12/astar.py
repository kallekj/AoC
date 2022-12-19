import numpy as np
from queue import PriorityQueue
from node import Node

class Astar():

    def __init__(self) -> None:
        self.queue = PriorityQueue()
        self.visited = set()
        self.path = []
        self.searchedNodes = 0

    def search(self, the_map, start: Node, goal: Node):

        def _cost_function(cords, goal: Node) -> int:
            return np.abs(goal.pos[0] - cords[0]) + np.abs(goal.pos[1] - cords[1])

        def _cord_is_within_map(cord, the_map):
            a = (cord[0] < the_map.shape[0]) and (cord[0] > -1)
            b = (cord[1] < the_map.shape[1]) and (cord[1] > -1)
            return a and b

        def _can_visit_neighbor(current: Node, neighbor, the_map):
            current_pos_value = the_map[current.pos[0]][current.pos[1]]
            neighbor_pos_value = the_map[neighbor[0]][neighbor[1]]
            return neighbor_pos_value <= current_pos_value + 1

        def _get_neighbors(current: Node, the_map):
            x = current.pos[0]
            y = current.pos[1]

            neighbors = []

            for cord in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                if _cord_is_within_map(cord, the_map):
                    if _can_visit_neighbor(current, cord, the_map):
                        cost = _cost_function(
                            cord, goal) + current.depth + 1 + the_map[cord[0]][cord[1]]
                        new_node = Node(cord, current, cost, current.depth + 1)
                        neighbors.append(new_node)

            return neighbors

        def _get_path():
            thePath = []
            theNode = goal
            while theNode.pos != start.pos:
                thePath.append(theNode.pos)
                theNode = theNode.parent
            return thePath

        self.queue.put(start)

        while not self.queue.empty():
            current: Node = self.queue.get()

            if current.pos == goal.pos:
                goal.parent = current
                self.path = _get_path()
                break

            for next_node in _get_neighbors(current, the_map):

                if next_node not in self.visited:
                    self.searchedNodes += 1
                    self.queue.put(next_node)
                    self.visited.add(next_node)
        
        return self.path
