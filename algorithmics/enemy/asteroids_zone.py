from typing import List

from algorithmics.enemy.enemy import Enemy
from algorithmics.utils.coordinate import Coordinate


class AsteroidsZone(Enemy):

    def __init__(self, boundary: List[Coordinate]):
        """Initializes a new asteroids zone area

        :param boundary: list of coordinates representing the boundary of the asteroids zone
        """
        self.boundary = boundary

    def convert_to_array(self):
        points_array = []
        for coord in self.boundary:
            points_array.append([coord.x, coord.y])
        return points_array
