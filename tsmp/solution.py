from tsmp.path import Path


class Solution:

    def __init__(self, map):
        self.map = map
        self.longest_path = None
        self.longest_distance = 0.0
        self.shortest_path = None
        self.shortest_distance = 0.0
        self.best_path_list = list()
        self.path_list = list()

    def run(self):
        print(len(self.path_list))
