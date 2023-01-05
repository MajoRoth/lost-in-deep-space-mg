from typing import List, Tuple

import algorithmics.utils.coordinate
from algorithmics.enemy.radar import Radar
from algorithmics.utils.coordinate import Coordinate
import numpy as np


ARG_RES = 5
RAD_RES = 5


def polar_to_cart(origin, rad, arg):
    x = rad * np.cos(arg) + origin.x
    y = rad * np.sin(arg) + origin.y
    return Coordinate(x, y)


def discrete_radar_graph(radar_list: List[Radar], point_to_find = []):
    nodes = []
    edges = []

    nodes += point_to_find

    for radar in radar_list:
        for i in range(0, ARG_RES):
            for j in range(1, RAD_RES + 1):
                coor = polar_to_cart(radar.center, j*radar.radius/RAD_RES, i*2*np.pi/ARG_RES)
                nodes.append(coor)

    for u in nodes:
        for v in nodes:
            if check_if_edge_is_legal(radar_list, u, v):
                edges.append((u, v))

    return nodes, edges


def check_if_edge_is_legal(radar_list: List[Radar], u: Coordinate, v: Coordinate):
    for radar in radar_list:
        in_range = (u.distance_to(radar.center) <= radar.radius or v.distance_to(radar.center) <= radar.radius)
        if in_range and (abs(algorithmics.utils.coordinate.angle(u, radar.center, v)) < 45):
            return False
    return True


if __name__ == '__main__':
    u = Coordinate(1/2,1/2)
    v = Coordinate(0,1)
    print(algorithmics.utils.coordinate.angle(v, Coordinate(0,0), u))