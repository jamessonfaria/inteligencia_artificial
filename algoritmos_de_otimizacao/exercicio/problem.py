from algoritmos_de_otimizacao.exercicio.fitness import fitness_function
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose


def print_solution(solution):
    total = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total += products[i][2]
            print('%s - %s' % (products[i][0], products[i][2]))

    print('Total >>>> %s' % (total))


products = [('Refrigerador A', 0.751, 999.90),
            ('Celular', 0.0000899, 2911.12),
            ('TV 55', 0.400, 4346.99),
            ('TV 50', 0.290, 3999.90),
            ('TV 42', 0.200, 2999.00),
            ('Notebook A', 0.00350, 2499.90),
            ('Ventilador', 0.496, 199.90),
            ('Microondas A', 0.0424, 308.66),
            ('Microondas B', 0.0544, 429.90),
            ('Microondas C', 0.0319, 299.29),
            ('Refrigerador B', 0.635, 849.00),
            ('Refrigerador C', 0.870, 1199.89),
            ('Notebook B', 0.498, 1999.90),
            ('Notebook C', 0.527, 3999.00)]

maximum_capacity = 3


def get_problem():
    fitness = mlrose.CustomFitness(fitness_function)
    return mlrose.DiscreteOpt(length=14, fitness_fn=fitness, maximize=True, max_val=2)

