from typing import TypedDict
import random
import string

class Excalidraw(TypedDict):
    type: str
    version: int
    elements: list

ids = []
def generate_id() -> str:
    tries = 0
    while True:
        if tries == 10:
            raise Exception("Could not generate a unique ID in 10 tries")
        id =  ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        tries += 1
        if id not in ids:
            ids.append(id)
            return id
def generate_seed():
    return 1929921419

def get_base():
    # Default values can be overridden in params
    return {
        "id": generate_id(),
        "version": 1,
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "roundness": None,
        "frameId": None,
        "seed": generate_seed(),
        "versionNonce": generate_seed(),
        "isDeleted": False,
        "boundElements": None,
        # "updated": TODO
        "link": None,
        "locked": False,
        "angle": 0,
        "strokeColor": "#1e1e1e",
        "backgroundColor": "transparent",
    }

def generate_text_element(x, y, text, **kwargs):
    element = get_base()
    element["fontSize"] = 20
    element["fontFamily"] = 1
    element.update(kwargs)

    width = element['fontSize'] * len(text) // 1.45
    height = int(element['fontSize'] * 1.25)

    element.update({
        "type": "text",
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "text": text,
        "textAlign": "center",
        "verticalAlign": "middle",
        "containerId": None,
        "originalText": text,
        "lineHeight": 1.25,
    })
    centerx = x + (width // 2)
    centery = y + (height // 2)
    return element, centerx, centery

# Generate arrow element and bind it to the start and end elements
def generate_arrow_element(x1, y1, x2, y2, start_element, end_element, **kwargs):
    element = get_base()
    element.update(kwargs)

    def generate_binding(id):
        return {
            "elementId": id,
            "focus": 0,
            "gap": 10
        }
    
    if start_element:
        if not start_element["boundElements"]:
            start_element["boundElements"] = []
        
        start_element["boundElements"].append({
            "id": element["id"],
            "type": "arrow"
        })
    
    if end_element:
        if not end_element["boundElements"]:
            end_element["boundElements"] = []
        
        end_element["boundElements"].append({
            "id": element["id"],
            "type": "arrow"
        })

    element.update({
        "type": "arrow",
        "x": x1,
        "y": y1,
        "width": abs(y1-y2),
        "height": abs(x1-x2),
        "roundness": {
            "type": 2
        },
        "points": [
            [0, 0],
            [x2-x1, y2-y1],
        ],
        "lastCommitedPoint": None,
        "startBinding": generate_binding(start_element["id"] if start_element else None),
        "endBinding": generate_binding(end_element["id"] if start_element else None),
        "startArrowhead": None,
        "endArrowhead": "arrow"
    })

    return element

def generate_excalidraw(nodes, topics):
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
        element, x, y = generate_text_element(
            node.position['x'],
            node.position['y'],
            topics[node.id]
        )
        excalidraw["elements"].append(element)
        node.element = element
        node.center = (x, y)

    # Draw the arrows
    for node in nodes:
        def node_from_id(id: str):
            return next((node for node in nodes if node.id == id), None)
        
        for edgeid in node.edges:
            edge = node_from_id(edgeid)
            x1, y1, x2, y2 = node.center[0], node.center[1], edge.center[0], edge.center[1]

            a, b = 1, 6 # Divide line in a ratio so line doesn't start from inside the text
            startx = (b * x1 + a * x2) // (a + b)
            starty = (b * y1 + a * y2) // (a + b)
            a, b = b, a
            endx = (b * x1 + a * x2) // (a + b)
            endy = (b * y1 + a * y2) // (a + b)

            excalidraw["elements"].append(generate_arrow_element(
                startx, starty, endx, endy, node.element, edge.element
            ))

    return excalidraw