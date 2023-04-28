import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade) -> None:
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor esta vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' -> ', self.valores[i])

    # O(n)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade maxima atingida')
            return
    
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        ultima_posicao = self.ultima_posicao
        while ultima_posicao >= posicao:
            self.valores[ultima_posicao + 1] = self.valores[ultima_posicao]
            ultima_posicao -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1
            
vetor = VetorOrdenado(10)
vetor.insere(6)
vetor.insere(4)
vetor.insere(3)
vetor.insere(5)
vetor.insere(1)
vetor.insere(8)
vetor.insere(2)
vetor.imprime()