from tsmp.node import Node
from tsmp.settings import MAP_SIZE_Y, MAP_SIZE_X


class Map:

    def __init__(self, node_count=6):
        self.size_x = MAP_SIZE_X
        self.size_y = MAP_SIZE_Y
        if node_count <= 1:
            self.node_count = 2
        else:
            self.node_count = node_count
        self.node_list = list()
        for i in range(self.node_count):
            self.node_list.append(Node(id=i))

    def get_distance_from_path(self, path):
        distance = 0.0
        for i in range(self.node_count):
            if i < self.node_count - 1:
                distance += self.node_list[path.node_order_list[i]].get_distance_to_node(self.node_list[path.node_order_list[i+1]])
                pass
        return distance

    def reset_node_weight(self):
        for i in range(self.node_count):
            self.node_list[i].weight = 0.0
