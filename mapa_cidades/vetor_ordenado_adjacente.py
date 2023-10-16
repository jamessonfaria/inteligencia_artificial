import numpy as np

from mapa_cidades.grafo import grafo


class AdjacentOrderedVector:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.last_position = -1
        self.values = np.empty(self.capacity, dtype=object)

    # O(n)
    def print(self):
        if self.last_position == -1:
            print('O vetor esta vazio')
        else:
            for i in range(self.last_position + 1):
                print(i, ' -> ', self.values[i].vertice.rotulo, ' - ',
                      self.values[i].custo, ' - ',
                      self.values[i].vertice.distancia_objetivo, ' - ',
                      self.values[i].distancia_aestrela)

    # O(n)
    def insert(self, adjacente):
        if self.last_position == self.capacity - 1:
            print('Capacidade maxima atingida')
            return

        posicao = self.__get_position(adjacente)
        self.__change_positions(posicao)

        self.values[posicao] = adjacente
        self.last_position += 1

    def __get_position(self, adjacente):
        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i].distancia_aestrela > adjacente.distancia_aestrela:
                break
            if i == self.last_position:
                position = i + 1
        return position

    def __change_positions(self, position):
        last_position = self.last_position
        while last_position >= position:
            self.values[last_position + 1] = self.values[last_position]
            last_position -= 1
