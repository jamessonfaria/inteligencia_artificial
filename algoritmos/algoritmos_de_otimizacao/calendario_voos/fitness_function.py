import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose


def fitness_function(agenda):
    from algoritmos_de_otimizacao.calendario_voos.representacao_problema import pessoas, voos, destino
    id_voo = -1
    total_preco = 0
    for i in range(len(agenda) // 2):
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][agenda[id_voo]]
        total_preco += ida[2]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        total_preco += volta[2]

    return total_preco


def get_problema():
    fitness = mlrose.CustomFitness(fitness_function)
    return mlrose.DiscreteOpt(length=12, fitness_fn=fitness, maximize=False, max_val=10)

