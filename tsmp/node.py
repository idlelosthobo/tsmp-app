from random import randint
from tsmp.settings import MAP_SIZE_X, MAP_SIZE_Y
from math import sqrt


class Node:

    def __init__(self, x=None, y=None):
        if x:
            self.x = x
        else:
            self.x = randint(0, MAP_SIZE_X)

        if y:
            self.y = y
        else:
            self.y = randint(0, MAP_SIZE_Y)

    def get_distance_to_node(self, node):
        distance = sqrt((self.x - node.x) ** 2 + (self.y - node.y) ** 2)
        return distance
