from typing import List, TypedDict
from math import log, sqrt

# Adjust parameters to your liking
c1 = 30; # How fast strings snap
c2 = 150; # Ideal distance between adjacent nodes
c3 = 2000; # Force between non-adjacent nodes
c4 = 0.4; # Overall delta-displacement based on forces

class Position(TypedDict):
    x: float
    y: float

class Node:
    def __init__(self, id: str, position: Position, edges: List[str]):
        self.id = id
        self.position = position
        self.edges = edges
        self.forces = []
    pass

# Graph is supposed to be unidirectional
# A->B will automatically include attractive forces for both A->B and B->A
# Edge A->B and B->A, if included, will produce two times as much force
def force_directed_layout(nodes: List[Node], iterations: int):
    def dist(x1, y1, x2, y2):
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def node_from_id(id: str):
        return next((node for node in nodes if node.id == id), None)

    for _ in range(iterations):
        # Zero out forces from previous iteration
        for i in range(len(nodes)):
            nodes[i].forces = []

        # Calculate forces
        for node in nodes:
            # Spring force for edges
            for edgeid in node.edges:
                edge = node_from_id(edgeid)
                d = dist(
                    node.position['x'], node.position['y'],
                    edge.position['x'], edge.position['y']
                )
                forceMag = c1 * log(d / c2)
                forceAngle: Position = {
                    'x': (edge.position['x'] - node.position['x']) / d,
                    'y': (edge.position['y'] - node.position['y']) / d,
                }
                node.forces.append({ 'magnitude': forceMag, 'angle': forceAngle })
                edge.forces.append({ 'magnitude': -forceMag, 'angle': forceAngle })

            # Inverse square forces on all other nodes
            for other in nodes:
                # If current node or edge ignore
                if node.id == other.id or other.id in node.edges or node.id in other.edges: continue

                d = dist(
                    node.position['x'], node.position['y'],
                    other.position['x'], other.position['y']
                )
                forceMag = c3 / (d ** 1.4)
                forceAngle = {
                    'x': (node.position['x'] - other.position['x']) / d,
                    'y': (node.position['y'] - other.position['y']) / d
                }
                node.forces.append({ 'magnitude': forceMag, 'angle': forceAngle })

        # Apply forces
        for node in nodes:
            for force in node.forces:
                node.position['x'] += c4 * force['magnitude'] * force['angle']['x']
                node.position['y'] += c4 * force['magnitude'] * force['angle']['y'] * 1.5

if __name__ == '__main__':
    nodes: List[Node] = [
        Node('A', {'x': 189, 'y': 198}, ['B', 'C', 'E']),
        Node('B', {'x': 198, 'y': 539}, []),
        Node('C', {'x': 208, 'y': 220}, []),
        Node('D', {'x': 50, 'y': 243}, ['E']),
        Node('E', {'x': 449, 'y': 203}, [])
    ]
    force_directed_layout(nodes, 150)
    for node in nodes:
        print(f"{node.id} {node.position['x']} {node.position['y']}")

    """
    From javascript visualization
    Starting configuration: 
        A 189 198
        B 198 539
        C 208 220
        D 50 243
        E 449 203
    Expected configuration: 
        A 261.75497728940644 363.39472633706873
        B 138.25832312191721 473.1206271175769
        C 386.0912085460245 467.49961804196954
        D 185.1510878093711 81.2947076335638
        E 293.3409433433769 197.9445308447649
    """
    pass
