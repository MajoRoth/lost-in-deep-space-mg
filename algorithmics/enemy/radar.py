import algorithmics.utils.coordinate

from algorithmics.enemy.enemy import Enemy
from algorithmics.utils.coordinate import Coordinate


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


