import shapely
from algorithmics.utils import coordinate
from algorithmics.enemy import asteroids_zone, black_hole


def check_for_line_and_plygon(line: [[float, float], [float, float]], shape: asteroids_zone):
    poly = shapely.geometry.polygon(shape.convert_to_array())
    l = shapely.geometry.LineString(line)
    return l.intersects(poly)


def check_for_line_and_circle(line: [[float, float], [float, float]], shape: black_hole):
    circle = shapely.geometry.Point(shape.center.x, shape.center.y).buffer(shape.radius)
    l = shapely.geometry.LineString(line)
    return l.intersects(circle)


def check_for_line_and_multiple_enemies(line:  [[float, float], [float, float]], enemies_array):
    for enemy in enemies_array:
        if type(enemy) == asteroids_zone and not check_for_line_and_plygon(line, enemy):
            return False
        elif type(enemy) == black_hole and not check_for_line_and_circle(line, enemy):
            return False
    return True
