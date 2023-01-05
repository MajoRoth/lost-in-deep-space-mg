from typing import List, Tuple

import networkx as nx

from algorithmics.enemy.asteroids_zone import AsteroidsZone
from algorithmics.enemy.enemy import Enemy
from algorithmics.solution.line_intersects import check_for_line_and_multiple_enemies
from algorithmics.utils.coordinate import Coordinate


# Navigator


def calculate_path(source: Coordinate, targets: List[Coordinate], enemies: List[Enemy], allowed_detection: float = 0) \
        -> Tuple[List[Coordinate], nx.Graph]:
    """Calculates a path from source to target without any detection

    Note: The path must start at the source coordinate and end at the target coordinate!

    :param source: source coordinate of the spaceship
    :param targets: target coordinate of the spaceship
    :param enemies: list of enemies along the way
    :param allowed_detection: maximum allowed distance of radar detection
    :return: list of calculated path waypoints and the graph constructed
    """
    print(source)
    print(targets)
    graph = nx.DiGraph()
    graph.add_node(source)  # add node for source
    graph.add_node(targets[0])  # add node for first target

    """
        build nodes for each enemy
    """
    for enemy in enemies:
        if isinstance(enemy, AsteroidsZone):
            for coor in enemy.boundary:
                graph.add_node(coor)

    for u in graph.nodes:
        for v in graph.nodes:
            if check_for_line_and_multiple_enemies(u, v, enemies):
                print("added node from {} to {}".format(str(u), str(v)))
                graph.add_edge(u, v, weight=u.distance_to(v))

            else:
                print("DIDNT add node from {} to {}".format(str(u), str(v)))

    print(graph.nodes)
    print(graph.edges)






    print(nx.Graph)




    return [source] + targets, graph
