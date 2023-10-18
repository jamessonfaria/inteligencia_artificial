from algoritmos_de_otimizacao.calendario_voos import hill_climb, fitness_function

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

melhor_solucao, melhor_custo = hill_climb.get_solucao(problema)
fitness_function.imprimir_voos(melhor_solucao)
