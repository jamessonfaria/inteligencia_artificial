import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose


def get_solution(problem):
    return mlrose.simulated_annealing(problem)
