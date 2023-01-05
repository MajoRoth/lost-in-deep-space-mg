import Christofides as Christofides


def solve_for_multiple_targets(distance_matrix):
    TSP = Christofides.christofides.compute(distance_matrix)
    return TSP['Chistofides_Solution']
