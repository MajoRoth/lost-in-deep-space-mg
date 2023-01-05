from typing import List
import math
from algorithmics.enemy.black_hole import BlackHole
from algorithmics.utils.coordinate import Coordinate


def get_circle_nodes(circle: BlackHole, n=20, eps = math.pow(10, -10)) -> List[Coordinate]:
    r = circle.radius + eps
    print (r)
    print (eps)
    x0 = circle.center.x
    y0 = circle.center.y
    t = math.pi/n
    a = r/math.cos(t)
    cord_lst = []
    for i in range (n):
        x = x0 + a*math.cos(2*i*t)
        y = y0 + a*math.sin(2*i*t)
        cord = Coordinate(x, y)
        cord_lst.append(cord)
    return cord_lst