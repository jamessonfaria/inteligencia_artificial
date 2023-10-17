class Vertex:
    def __init__(self, label, distance_objective):
        self.label = label
        self.distance_objective = distance_objective
        self.visited = False
        self.list_of_adjacent = []

    def add_adjacent(self, adjacent):
        self.list_of_adjacent.append(adjacent)

    def print_adjacent(self):
        for i in self.list_of_adjacent:
            print(i.vertex.label, i.cost)
            