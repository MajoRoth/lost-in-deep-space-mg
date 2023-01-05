import algorithmics.utils.coordinate
import numpy as np

from algorithmics.enemy.enemy import Enemy
from algorithmics.utils.coordinate import Coordinate


def polar_to_cart(origin, rad, arg):
    x = rad * np.cos(arg) + origin.x
    y = rad * np.sin(arg) + origin.y
    return Coordinate(x, y)


class Radar(Enemy):

    def __init__(self, center: Coordinate, radius: float):
        """Initializes a radar object at the location with the given detection radius

        :param center: location of the radar
        :param radius: detection radius of the radar
        """
        self.center = center
        self.radius = radius

    def shortest_pass(self, coor1, coor2):
        string = algorithmics.utils.coordinate.string(coor1, coor2)
        radial = string(coor1, self.center)
        if abs(algorithmics.utils.coordinate.angle(self.center, coor1, coor2)) >= 45:
            return (coor1, coor2)

    def discrete_perimeter(self, angular_res):
        nodes = []
        for i in range(0, angular_res):
            nodes.append(polar_to_cart(self.center, self.radius, i*2*np.pi/angular_res))
        return nodes

if __name__ == '__main__':
    radar = Radar(Coordinate(0,0), 5)
    print(radar.discrete_perimeter(12))


