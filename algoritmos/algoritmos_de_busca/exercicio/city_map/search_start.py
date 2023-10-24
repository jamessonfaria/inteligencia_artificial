from city_map.graph import Graph
from vector.ordered_vector import OrderedVector


class SearchStar:
    def __init__(self, goal):
        self.goal = goal
        self.found = False

    def search(self, current):
        print('------------')
        print('Current: {}'.format(current.label))
        current.visited = True

        if current == self.goal:
            self.found = True
        else:
            ordered_vector = OrderedVector(len(current.list_of_adjacent))
            for adjacent in current.list_of_adjacent:
                if not adjacent.vertex.visited:
                    adjacent.vertex.visited = True
                    ordered_vector.insert(adjacent)
            ordered_vector.print()

            if ordered_vector.values[0] is not None:
                self.search(ordered_vector.values[0].vertex)


search_star = SearchStar(Graph.bucharest)
search_star.search(Graph.arad)
