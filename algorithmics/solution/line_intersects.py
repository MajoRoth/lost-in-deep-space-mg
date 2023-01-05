import math
from typing import List

import shapely.geometry

from algorithmics.enemy.asteroids_zone import AsteroidsZone
from algorithmics.enemy.black_hole import BlackHole
from algorithmics.enemy.enemy import Enemy
from algorithmics.utils import coordinate
from algorithmics.enemy import asteroids_zone, black_hole
from algorithmics.utils.coordinate import Coordinate


def check_for_line_and_polygon(line: [[float, float], [float, float]], shape: AsteroidsZone):
    poly = shapely.geometry.Polygon(shape.convert_to_array())
    l = shapely.geometry.LineString(line)
    return l.within(poly)


def check_for_line_and_circle(line: [[float, float], [float, float]], shape: BlackHole):
    circle = shapely.geometry.Point(shape.center.x, shape.center.y).buffer(shape.radius)
    l = shapely.geometry.LineString(line)
    return l.within(circle)


def check_for_line_and_multiple_enemies(source: Coordinate, dest: Coordinate, enemies: List[Enemy]):
    line = [[source.x, source.y], [dest.x, dest.y]]
    length = math.sqrt(math.pow(line[0][0] - line[1][0], 2) + math.pow(line[0][1] - line[1][1], 2))
    if length == 0:
        return False
    for enemy in enemies:
        if type(enemy) == AsteroidsZone and check_for_line_and_polygon(line, enemy):
            return False
        elif type(enemy) == BlackHole and check_for_line_and_circle(line, enemy):
            return False
    return length


if __name__ == '__main__':
    source = Coordinate(0, 0)
    dest = Coordinate(5, 3)
    bh1 = BlackHole(Coordinate(10, 0), 3)
    bh2 = BlackHole(Coordinate(5, 5), 2)
    bh3 = BlackHole(Coordinate(12,12), 1)
    bh4 = BlackHole(Coordinate(-2, -2), 1)
    az1 = AsteroidsZone([Coordinate(3, 0), Coordinate(3, 10), Coordinate(10, 5)])
    az2 = AsteroidsZone([Coordinate(-2, -1), Coordinate(-3, -1), Coordinate(-2, -2)])
    az3 = AsteroidsZone([Coordinate(0, 0), Coordinate(0, 10), Coordinate(10, 10), Coordinate(10, 0)])
    az4 = AsteroidsZone([Coordinate(-10, -10), Coordinate(-10, 20), Coordinate(20, 20), Coordinate(20, -10)])
    az5 = AsteroidsZone([Coordinate(0, 3), Coordinate(5, 3), Coordinate(5, 10), Coordinate(0, 10)])
    az6 = AsteroidsZone([Coordinate(0, 0), Coordinate(0, 10), Coordinate(10, 10)])

    enems = [bh1, bh3, bh4, az2, az6]
    print(check_for_line_and_multiple_enemies(source, dest, enems))
