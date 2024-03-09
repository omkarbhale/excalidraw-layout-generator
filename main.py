from typing import List, TypedDict
import json
from force_directed_layout import Node, force_directed_layout
from utils import generate_text_element

class Excalidraw(TypedDict):
    type: str
    version: int
    elements: list

nodes: List[Node] = [
    Node('A', {'x': 189, 'y': 198}, ['B', 'C', 'E']),
    Node('B', {'x': 198, 'y': 539}, []),
    Node('C', {'x': 208, 'y': 220}, []),
    Node('D', {'x': 50, 'y': 243}, ['E']),
    Node('E', {'x': 449, 'y': 203}, [])
]

topics = {
    'A': "Computer Science",
    'B': "Object-Oriented Programming",
    'C': "Operating Systems",
    'D': "Waste Management",
    'E': "E-dustbins",
}

force_directed_layout(nodes)

excalidraw: Excalidraw = {
    "type": "excalidraw",
    "source": "https://excalidraw.com",
    "version": 1,
    "elements": [],
    "appState": {
        "gridSize": None,
        "viewBackgroundColor": "#ffffff"
    },
    "files": {}
}

# Write the text
for node in nodes:
    excalidraw["elements"].append(generate_text_element(
        node.position['x'],
        node.position['y'],
        topics[node.id]
    ))

with open('output.excalidraw', 'w') as output_file:
    json.dump(excalidraw, output_file, indent=4)

if __name__ == "__main__":
    pass