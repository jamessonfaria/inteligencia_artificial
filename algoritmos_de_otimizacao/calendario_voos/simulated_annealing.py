import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose


def get_solucao(problema):
    return mlrose.simulated_annealing(problema,
                                      schedule=mlrose.decay.GeomDecay(init_temp=10000),
                                      random_state=1)
