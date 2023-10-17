import numpy as np


class OrderedVector:
    def __init__(self, capacity):
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=object)

    def print(self):
        if self.last_position == -1:
            print("The vertex is empty")
        else:
            for i in range(self.last_position + 1):
                print(i, ' -> ', self.values[i].vertex.label, ' - ',
                      self.values[i].cost, ' - ',
                      self.values[i].vertex.distance_objective, ' - ',
                      self.values[i].distance_to_star)

    def insert(self, adjacent):
        if self.last_position == self.capacity - 1:
            print('Maximum capacity reached')
            return

        position = self.__get_position(adjacent)
        self.__change_positions(position)

        self.values[position] = adjacent
        self.last_position += 1

    def __get_position(self, adjacent):
        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i].distance_to_star > adjacent.distance_to_star:
                break
            if i == self.last_position:
                position = i + 1
        return position

    def __change_positions(self, position):
        last_position = self.last_position
        while last_position >= position:
            self.values[last_position + 1] = self.values[last_position]
            last_position -= 1
