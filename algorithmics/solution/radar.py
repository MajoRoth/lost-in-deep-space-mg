from typing import List, Tuple

import algorithmics.utils.coordinate
from algorithmics.enemy.radar import Radar
from algorithmics.utils.coordinate import Coordinate
import numpy as np
import tqdm

ARG_RES = 12
RAD_RES = 20


def polar_to_cart(origin, rad, arg):
    x = rad * np.cos(arg) + origin.x
    y = rad * np.sin(arg) + origin.y
    return Coordinate(x, y)


def discrete_radar_graph(radar_list: List[Radar], point_to_find):
    nodes = []
    edges = []
    perimeter = []

    for i in point_to_find:
        nodes.append((i, 500))

    for radar in radar_list:
        for i in range(0, ARG_RES):
            for j in range(1, RAD_RES + 1):
                coor = polar_to_cart(radar.center, j*radar.radius/RAD_RES, i*2*np.pi/ARG_RES)
                nodes.append((coor, i))
                if j == RAD_RES:
                    perimeter.append((coor, i))
    for u in nodes:
        for v in nodes:
            if check_if_edge_is_legal(radar_list, u[0], v[0]) and v[1] != u[1] and v[1] % 6 != u[1] % 6:
                edges.append((u[0], v[0]))

    new_node = list()
    perimeter_new = list()

    for node in nodes:
        new_node.append(node[0])

    for peri in perimeter:
        perimeter_new.append(peri[0])

    return new_node, edges, perimeter_new


def check_if_edge_is_legal(radar_list: List[Radar], u: Coordinate, v: Coordinate):
    for radar in radar_list:
        in_range = (u.distance_to(radar.center) <= radar.radius or v.distance_to(radar.center) <= radar.radius)
        if in_range and ((abs(algorithmics.utils.coordinate.angle(radar.center, u, v)) < 45) or (abs(algorithmics.utils.coordinate.angle(radar.center, v, u)) < 45)):
            return False
        elif u == radar.center or v == radar.center:
            return False
    return True


if __name__ == '__main__':
    o, u, v, w = Coordinate(0,0), Coordinate(3,0), Coordinate(0,3), Coordinate (0, -6)
    radar = Radar(o, 5)
    nodes, edges, perimeter = discrete_radar_graph([radar], [u,v,w])

    print()
