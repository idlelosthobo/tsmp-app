from tsmp.solutions.solution import Solution
from tsmp.path import Path


class Basic(Solution):

    def __init__(self, map):
        super().__init__(map)
        # self.permutation_list = permutations(range(self.map.node_count), self.map.node_count)
        # for permuation in self.permutation_list:
        self.path_list.append(Path(tuple(range(self.map.node_count))))
        self.add_information('Basic', 'Run')
