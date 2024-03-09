from typing import List, TypedDict
import json
from force_directed_layout import Node, force_directed_layout
from utils import generate_excalidraw
import random

# Example usage
if __name__ == "__main__":
    # Node(id, position, edges)
    # Give random starting positions between -300, 300
    nodes: List[Node] = [
        Node('A', {'x': random.randint(-300, 300), 'y': random.randint(-300, 300)}, ['B', 'C', 'E']),
        Node('B', {'x': random.randint(-300, 300), 'y': random.randint(-300, 300)}, []),
        Node('C', {'x': random.randint(-300, 300), 'y': random.randint(-300, 300)}, []),
        Node('D', {'x': random.randint(-300, 300), 'y': random.randint(-300, 300)}, ['E']),
        Node('E', {'x': random.randint(-300, 300), 'y': random.randint(-300, 300)}, [])
    ]

    topics = {
        'A': "Computer Science",
        'B': "Object-Oriented Programming",
        'C': "Operating Systems",
        'D': "Waste Management",
        'E': "E-dustbins",
    }

    # Create a nice layout
    force_directed_layout(nodes)

    # Generate the excalidraw file
    excalidraw = generate_excalidraw(nodes, topics)

    # Write the file to disk
    with open('output.excalidraw', 'w') as output_file:
        json.dump(excalidraw, output_file, indent=4)
