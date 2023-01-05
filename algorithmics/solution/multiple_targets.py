import Christofides as Christofides

from algorithmics import navigator


def solve_for_multiple_targets(targets, enemies, allowed_detection=0):
    distance_matrix = make_distance_matrix(targets, enemies, allowed_detection)
    TSP = Christofides.christofides.compute(distance_matrix)
    return TSP['Chistofides_Solution']


def make_distance_matrix(targets, enemies, allowed_detection=0):
    mat = []
    for node1 in targets:
        distances_from_target = []
        for node2 in targets:
            distances_from_target += navigator.calculate_path_single_dest(node1, node2, enemies, allowed_detection)
        mat += distances_from_target
    return mat

# def calculate_path_single_dest(source: Coordinate, target: Coordinate, enemies: List[Enemy], allowed_detection:
# float = 0) -> float: pass
