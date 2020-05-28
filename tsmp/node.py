from random import randint
from tsmp.settings import MAP_SIZE
from math import sqrt


class Node:

    def __init__(self, x=None, y=None):
        if x:
            self.x = x
        else:
            self.x = randint(0, MAP_SIZE)

        if y:
            self.y = y
        else:
            self.y = randint(0, MAP_SIZE)

    def get_distance_to(self, node):
        distance = sqrt((self.x - node.x) ** 2 + (self.y - node.y) ** 2)
        return distance