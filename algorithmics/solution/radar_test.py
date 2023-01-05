import matplotlib.pyplot as plt

from algorithmics.enemy.radar import Radar
from algorithmics.solution.radar import discrete_radar_graph
from algorithmics.utils.coordinate import Coordinate


def plot_node(point):
    plt.plot([point[0].x], [point[0].y], 'ro')


def plot_edge(edge):
    plt.plot([edge[0].x, edge[1].x], [edge[0].y, edge[1].y])


def test_radar():
    cood = Coordinate(20, 1)
    radar = Radar(cood, 100)
    nodes, edges, perimeter = discrete_radar_graph([radar], [Coordinate(20, 50)])
    for node in nodes:
        plot_node(node)
    for edge in edges:
        plot_edge(edge)
    plt.show()


test_radar()