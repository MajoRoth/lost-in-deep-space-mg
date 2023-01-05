import math
from typing import List

import shapely

from algorithmics.enemy.enemy import Enemy
from algorithmics.utils import coordinate
from algorithmics.enemy import asteroids_zone, black_hole
from algorithmics.utils.coordinate import Coordinate


def check_for_line_and_polygon(line: [[float, float], [float, float]], shape: asteroids_zone):
    poly = shapely.geometry.polygon(shape.convert_to_array())
    l = shapely.geometry.LineString(line)
    return l.intersects(poly)


def check_for_line_and_circle(line: [[float, float], [float, float]], shape: black_hole):
    circle = shapely.geometry.Point(shape.center.x, shape.center.y).buffer(shape.radius)
    l = shapely.geometry.LineString(line)
    return l.intersects(circle)


def check_for_line_and_multiple_enemies(source: Coordinate, dest: Coordinate, enemies: List[Enemy]):
    line = [[source.x, source.y], [dest.x, dest.y]]
    length = math.sqrt(math.pow(line[0][0] - line[1][0], 2) + math.pow(line[0][1] - line[1][1], 2))
    if length == 0:
        return False
    for enemy in enemies:
        if type(enemy) == asteroids_zone and not check_for_line_and_polygon(line, enemy):
            return False
        elif type(enemy) == black_hole and not check_for_line_and_circle(line, enemy):
            return False
    return length
