from mapa_cidades.grafo import grafo
from mapa_cidades.vetor_ordenado import OrderedVector
from mapa_cidades.vetor_ordenado_adjacente import AdjacentOrderedVector


# Algoritmo de busca AEstrela ou A*
class BuscaAEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('------------------')
        print('Atual: {}'.format(atual.rotulo))
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = AdjacentOrderedVector(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if not adjacente.vertice.visitado:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insert(adjacente)
            vetor_ordenado.print()

            if vetor_ordenado.values[0] is not None:
                self.buscar(vetor_ordenado.values[0].vertice)


busca_estrela = BuscaAEstrela(grafo.bucharest)
busca_estrela.buscar(grafo.arad)
