def fitness_function(solution):
    from algoritmos_de_otimizacao.exercicio.problem import products, maximum_capacity

    cost = 0
    increase_space = 0

    for i in range(len(solution)):
        if solution[i] == 1:
            cost += products[i][2]
            increase_space += products[i][1]

    if increase_space > maximum_capacity:
        cost = 1

    return cost
