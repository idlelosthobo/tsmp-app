from tsmp.node import Node
from tsmp.settings import MAXIMUM_NODE_COUNT


class Map:

    def __init__(self, node_count=4):
        if node_count > MAXIMUM_NODE_COUNT:
            self.node_count = MAXIMUM_NODE_COUNT
        elif node_count <= 1:
            self.node_count = 2
        else:
            self.node_count = node_count
        self.node_list = dict()
        for i in range(self.node_count):
            self.node_list[i] = Node()

    def get_distance_from_path(self, path):
        for i in range(len(path)):