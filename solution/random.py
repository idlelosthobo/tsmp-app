from tsmp.solution import Solution
from tsmp.path import Path
from itertools import permutations
from random import shuffle


class Random(Solution):

    def __init__(self, map):
        super().__init__(map)
        path = list(range(self.map.node_count))
        for count in range(1000):
            shuffle(path)
            self.path_list.append(Path(tuple(path)))
