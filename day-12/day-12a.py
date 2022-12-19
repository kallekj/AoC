import numpy as np
from node import Node
from bfs import BFS

with open('./day-12/input') as f:
    the_map = np.array([[ord(char) for char in list(line.rstrip('\n'))]
                       for line in f.readlines()])

start = [np.where(the_map == 83)[0][0], np.where(the_map == 83)[1][0]]
goal = [np.where(the_map == 69)[0][0], np.where(the_map == 69)[1][0]]
the_map[start[0]][start[1]] = 96
the_map[goal[0]][goal[1]] = 123

start_node = Node(start, None, 0, 0)
goal_node = Node(goal, None, np.Inf, 0)

searcher = BFS()
path = searcher.search(the_map, start_node, goal_node)
print("Length of path: {}".format(len(searcher.path) - 1))
