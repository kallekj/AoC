import numpy as np
from node import Node
from bfs import BFS

with open('./day-12/input') as f:
    the_map = np.array([[ord(char) for char in list(line.rstrip('\n'))]
                       for line in f.readlines()])

S = [np.where(the_map == 83)[0][0], np.where(the_map == 83)[1][0]]
goal = [np.where(the_map == 69)[0][0], np.where(the_map == 69)[1][0]]
the_map[S[0]][S[1]] = 97
the_map[goal[0]][goal[1]] = 123

aIndexes = np.where(the_map == 97)
starts = list(map(lambda pos: Node(pos, None, 0, 0), zip(aIndexes[0], aIndexes[1])))
goal_node = Node(goal, None, np.Inf, 0)

searcher = BFS()
shortest_path = np.Inf
for start in starts:
    searcher = BFS()
    searcher.search(the_map, start, goal_node)
    if len(searcher.path) < shortest_path and len(searcher.path) > 0:
        shortest_path = len(searcher.path)

print("Length of path: {}".format(shortest_path - 1))
