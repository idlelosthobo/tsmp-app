from tsmp.solution import Solution
from tsmp.path import Path
from itertools import permutations
from random import randint


class Random(Solution):

    def __init__(self, map):
        super().__init__(map)
        self.permutation_list = permutations(range(self.map.node_count), self.map.node_count)
        for permuation in self.permutation_list:
            if randint(0,10) == 1:
                self.path_list.append(Path(permuation))
