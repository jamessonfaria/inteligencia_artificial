from algoritmos_de_otimizacao.exercicio import hill_climb, simulated_annealing, genetic_algorithm
from algoritmos_de_otimizacao.exercicio.problem import get_problem, print_solution

problem = get_problem()

print("---------solution using the Hill Climb ------------------")
best_solution1, best_cost1 = hill_climb.get_solution(problem)
print_solution(best_solution1, best_cost1)

print("---------solution using the Simulated Annealing ------------------")
best_solution2, best_cost2 = simulated_annealing.get_solution(problem)
print_solution(best_solution2, best_cost2)

print("---------solution using the Genetic Algorithm ------------------")
best_solution3, best_cost3 = genetic_algorithm.get_solution(problem)
print_solution(best_solution3, best_cost3)
