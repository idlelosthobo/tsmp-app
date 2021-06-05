from random import randint
from tsmp.settings import MAP_SIZE_X, MAP_SIZE_Y
from math import sqrt
import numpy as np


class Node:

    def __init__(self, id, x=None, y=None):
        self.id = id
        if x:
            self.x = x
        else:
            self.x = randint(0, MAP_SIZE_X)

        if y:
            self.y = y
        else:
            self.y = randint(0, MAP_SIZE_Y)

        self.weight = 0.0

    def get_distance_to_node(self, node):
        distance = sqrt((self.x - node.x) ** 2 + (self.y - node.y) ** 2)
        return distance

    def get_angle_to_node(self, node):
        p1 = (self.x, self.y)
        p2 = (node.x, node.y)
        ang1 = np.arctan2(*p1[::-1])
        ang2 = np.arctan2(*p2[::-1])
        return np.rad2deg((ang1 - ang2) % (2 * np.pi))
