import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose


def get_solucao(problema):
    return mlrose.hill_climb(problema, random_state=1)
