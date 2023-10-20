import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

## Antencedentes
valores_possiveis = np.arange(0, 11, 1)
qualidade = ctrl.Antecedent(valores_possiveis, 'qualidade')
servico = ctrl.Antecedent(valores_possiveis, 'servico')

## Consequentes
valores_possiveis = np.arange(0, 21, 1)
gorjeta = ctrl.Consequent(valores_possiveis, 'gorjeta')

## Membership functions (Mapeamento dos valores dentro das faixas)
qualidade.automf(number=3, names=['ruim', 'boa', 'saborosa'])
servico.automf(number=3, names=['ruim', 'aceitável', 'ótimo'])

## Definicao da faixa dos consequentes
gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 5])
gorjeta['media'] = fuzz.trimf(gorjeta.universe, [5, 10, 12])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [12, 20, 20])

# gorjeta['baixa'] = fuzz.sigmf(gorjeta.universe, 5, -1)
# gorjeta['media'] = fuzz.gaussmf(gorjeta.universe, 10, 3)
# gorjeta['alta'] = fuzz.pimf(gorjeta.universe, 10, 20, 20, 21)

## Regras para o controle do fuzzy
regra1 = ctrl.Rule(qualidade['ruim'] | servico['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(servico['aceitável'], gorjeta['media'])
regra3 = ctrl.Rule(qualidade['saborosa'] | servico['ótimo'], gorjeta['alta'])

## Definicao do sistema de controle
sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])
sistema = ctrl.ControlSystemSimulation(sistema_controle)

## Simulacao e previsao
sistema.input['qualidade'] = 8
sistema.input['servico'] = 9
sistema.compute()

print(sistema.output['gorjeta'])
gorjeta.view(sistema)

plt.show()