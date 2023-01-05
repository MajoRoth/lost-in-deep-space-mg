from typing import List, Tuple

import networkx as nx

from algorithmics.enemy.asteroids_zone import AsteroidsZone
from algorithmics.enemy.black_hole import BlackHole
from algorithmics.enemy.enemy import Enemy
from algorithmics.enemy.radar import Radar
from algorithmics.solution.circle import get_circle_nodes
from algorithmics.solution.line_intersects import check_for_line_and_multiple_enemies
from algorithmics.solution.radar import discrete_radar_graph
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
    graph = nx.DiGraph()
    route = list()
    path = [source] + targets

    for i in range(len(path)-1):
        partial_route, partial_graph = calculate_path_for_single(path[i], path[i+1], enemies, allowed_detection)
        route += partial_route

    return route, graph




def calculate_path_for_single(source: Coordinate, targets: Coordinate, enemies: List[Enemy], allowed_detection: float = 0) \
        -> Tuple[List[Coordinate], nx.Graph]:
    """Calculates a path from source to target without any detection

    Note: The path must start at the source coordinate and end at the target coordinate!

    :param source: source coordinate of the spaceship
    :param targets: target coordinate of the spaceship
    :param enemies: list of enemies along the way
    :param allowed_detection: maximum allowed distance of radar detection
    :return: list of calculated path waypoints and the graph constructed
    """
    graph = nx.DiGraph()
    graph.add_node(source)  # add node for source
    graph.add_node(targets)  # add node for first target

    """
        build nodes for each enemy
    """
    radar_list = []

    for enemy in enemies:
        if isinstance(enemy, AsteroidsZone):
            for coor in enemy.boundary:
                graph.add_node(coor)
        if isinstance(enemy, BlackHole):
            for node in get_circle_nodes(enemy):
                graph.add_node(node)
        if isinstance(enemy, Radar):
            radar_list.append(enemy)

    nodes, edges, perimeter = discrete_radar_graph(radar_list, [source, targets])

    for node in nodes:
        graph.add_node(node)

    for u, v in edges:
        if check_for_line_and_multiple_enemies(u, v, enemies, radar=False):
            graph.add_edge(u, v, weight=u.distance_to(v))


    for u in graph.nodes:
        for v in graph.nodes:
            if check_for_line_and_multiple_enemies(u, v, enemies):
                graph.add_edge(u, v, weight=u.distance_to(v))

    route = nx.shortest_path(graph, source=source, target=targets, weight='weight')

    return route, graph



