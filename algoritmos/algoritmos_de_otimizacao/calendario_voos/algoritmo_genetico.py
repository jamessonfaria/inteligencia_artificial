import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose


def get_solucao(problema):
    return mlrose.genetic_alg(problema, pop_size=500, mutation_prob=0.2, random_state=1)
