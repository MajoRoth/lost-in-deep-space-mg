
def next_target(current, unvisited):
    return max(unvisited, key=lambda target: dist_from_start_to_target(current, target))

def path_for_all_targets(start, targets):
    current = start
    path = [start]
    for i in targets:
        current = next_target(current, targets)
        path.append(current)
        targets.remove(current)
    return path

def dist_from_node1_to_node2(node1, node2):
    pass



def weights_matrix()
    G = []
    for node1 in range(nV):
        weights_from_node1 = []
        for node2 in range(nV):
            weights_from_node1 += dist_from_node1_to_node2(node1, node2)
        G += weights_from_node1

