from typing import List
from force_directed_layout import Node, Position, force_directed_layout

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

if __name__ == "__main__":
    pass