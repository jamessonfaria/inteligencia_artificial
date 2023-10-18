from algoritmos_de_otimizacao.calendario_voos import hill_climb, fitness_function, simulated_annealing


def imprimir_voos(agenda):
    from algoritmos_de_otimizacao.calendario_voos.representacao_problema import pessoas, voos, destino
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        nome = pessoas[i][0]
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]
        print('%10s%10s %5s-%5s %3s %5s-%5s %3s' % (nome, origem, ida[0], ida[1], ida[2],
                                                volta[0], volta[1], volta[2]))
    print('Preço total: ', total_preco)

pessoas = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'),
           ('Dublin', 'DUB'),
           ('Bruxelas', 'BRU'),
           ('Londres', 'LHR')]

destino = 'FCO'
voos = {}

for linha in open('flights.txt'):
    origem, destino, saida, chegada, preco = linha.split(',')
    voos.setdefault((origem, destino), [])
    voos[(origem, destino)].append((saida, chegada, int(preco)))

agenda = [1, 7, 3, 1, 1, 1, 6, 3, 2, 4, 5, 3]
valor = fitness_function.fitness_function(agenda)

problema = fitness_function.get_problema()

print("---------solucao usando o Hill Climb ------------------")
melhor_solucao, melhor_custo = hill_climb.get_solucao(problema)
imprimir_voos(melhor_solucao)

print("---------solucao usando o Simulated Annealing ------------------")
melhor_solucao, melhor_custo = simulated_annealing.get_solucao(problema)
imprimir_voos(melhor_solucao)
