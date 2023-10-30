import time
import gym
import random

import numpy as np

############ Entendimento do ambiente
# 0 = south, 1 = north, 2 = east, 3 = west, 4 = pickup, 5 = dropoff
env = gym.make('Taxi-v3', render_mode='ansi')
env.reset()
print(env.render())
print(env.action_space)
print(env.observation_space)
print(len(env.P))
print(env.P)
print(env.P[484])

############  Treinamento
# Q-learning => Qt(s,a) = Qt-1(s,a) + aTDt(a,s)
# 1-10% 3-90%
# exploration / exploitation

start_time = time.time()
from IPython.display import clear_output

alpha = 0.1
gamma = 0.6
epsilon = 0.1

for i in range(1000):
    estado = env.reset()
    estado = estado[0]
    penalidades, recompensa = 0, 0
    done = False
    q_table = np.zeros([env.observation_space.n, env.action_space.n])

    while not done:
        # Exploration
        if random.uniform(0, 1) < epsilon:
            acao = env.action_space.sample()
        # Exploitation
        else:
            acao = np.argmax(q_table[estado])

        proximo_estado, recompensa, done, info, type = env.step(acao)

        q_antigo = q_table[estado, acao]
        proximo_maximo = np.max(q_table[proximo_estado])

        q_novo = (1 - alpha) * q_antigo + alpha * (recompensa + gamma * proximo_maximo) ## (1 - alpha) * => é apenas para reduzir a escala
        q_table[estado, acao] = q_novo

        if recompensa == -10:
            penalidades += 1

        estado = proximo_estado

    if i % 100 == 0:
        clear_output(wait=False)
        print('Episodio: ', i)

end_time = time.time()
execution_time = end_time - start_time
print(f"Tempo de execução: {execution_time} segundos")
print('Treinamento concluido.')


############  Avaliação
total_penalidades = 0
episodios = 50
frames = []

for _ in range(episodios):
  estado = env.reset()
  estado = estado[0]
  penalidades, recompensa = 0, 0
  done = False
  while not done:
    acao = np.argmax(q_table[estado])
    estado, recompensa, done, info, _ = env.step(acao)

    if recompensa == -10:
      penalidades += 1

    frames.append({
        'frame': env.render(),
        'state': estado,
        'action': acao,
        'reward': recompensa
    })

  total_penalidades += penalidades

print('Episódios', episodios)
print('Penalidades', total_penalidades)