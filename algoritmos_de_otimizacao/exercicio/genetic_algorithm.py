import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose


def get_solution(problem):
    return mlrose.genetic_alg(problem, pop_size=500, mutation_prob=0.2)
