# a solution that checks angle change, path length and determines best route

from tsmp.solution import Solution
from tsmp.path import Path
from itertools import permutations


class WeightedAngle(Solution):

    def __init__(self, map, start_node):
        super().__init__(map)

        self.map = map
        self.start_node = start_node
        self.current_node = start_node

        self.used_node_list = dict()

        for i in range(self.map.node_count):
            self.used_node_list[i] = False

        self.used_node_list[self.start_node] = True

        self.weighted_path = list()
        self.weighted_path.append(self.start_node)

        self.get_next_node(self.start_node)

        self.path_list.append(Path(self.weighted_path))


    def get_next_node(self, node):
        next_node = None
        last_angle = None
        biggest_angle = None
        for i in range(len(self.used_node_list)):
            if not self.used_node_list[i]:
                first_angle = self.map.node_list[self.current_node].get_angle_to_node(self.map.node_list[i])
                for k in range(len(self.used_node_list)):
                    if not self.used_node_list[k] and k != i:
                        second_angle = self.map.node_list[k].get_angle_to_node(self.map.node_list[i])
                        print(str(i) + ' ' + str(first_angle) + ' ' + str(k) + ' ' + str(second_angle))
                        total_angle = first_angle + second_angle
                        if last_angle is None or biggest_angle is None:
                            last_angle = total_angle
                            biggest_angle = total_angle
                        if total_angle > biggest_angle:
                            next_node = i

        print('Next Node: ' + str(next_node))