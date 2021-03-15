class Path:

    def __init__(self, node_order_list):
        self.node_order_list = node_order_list
        self.distance = 0.0

    def __str__(self):
        return str(self.node_order_list)