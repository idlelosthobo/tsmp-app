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

    def set_longest(self, path, distance):
        self.longest_path = path
        self.longest_distance = distance

    def set_shortest(self, path, distance):
        self.shortest_path = path
        self.shortest_distance = distance

    def run(self):
        for path in self.path_list:
            distance = self.map.get_distance_from_path(path)
            if self.longest_distance is None:
                self.set_longest(path, distance)
            else:
                if self.longest_distance < distance:
                    self.set_longest(path, distance)

            if self.shortest_path is None:
                self.set_shortest(path, distance)
            else:
                if self.shortest_distance > distance:
                    self.set_shortest(path, distance)

        # print('Shortest Distance: ' + str(self.shortest_distance))
        # print('Longest Distance: ' + str(self.longest_distance))
