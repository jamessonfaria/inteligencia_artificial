class Adjacent:
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost
        self.distance_to_star = vertex.distance_objective + self.cost
