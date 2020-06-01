from tsmp.solution import Solution
from tsmp.path import Path
from itertools import permutations
from tsmp.settings import MAXIMUM_ACCURATE_NODE_COUNT, INACCURATE_SOLVE_ITTERATIONS
from random import shuffle

class Solve(Solution):

    def __init__(self, map):
        super().__init__(map)
        if self.map.node_count <= MAXIMUM_ACCURATE_NODE_COUNT:
            self.permutation_list = permutations(range(self.map.node_count), self.map.node_count)
            for permuation in self.permutation_list:
                self.path_list.append(Path(permuation))
        else:
            path = list(range(self.map.node_count))
            for count in range(INACCURATE_SOLVE_ITTERATIONS):
                shuffle(path)
                self.path_list.append(Path(tuple(path)))
