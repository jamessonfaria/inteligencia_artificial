from mapa_cidades.grafo import grafo
from mapa_cidades.vetor_ordenado import OrderedVector


class BuscaGulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('-----------')
        print('Atual: {}'.format(atual.rotulo))
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = OrderedVector(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if not adjacente.vertice.visitado:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insert(adjacente.vertice)
            vetor_ordenado.print()

            if vetor_ordenado.values[0] is not None:
                self.buscar(vetor_ordenado.values[0])


busca_gulosa = BuscaGulosa(grafo.bucharest)
busca_gulosa.buscar(grafo.arad)
