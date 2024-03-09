import random
import string

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

def generate_text_element(x, y, text, **kwargs):
    # Default values can be overridden in params
    args = {
        "version": 1,
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "angle": 0,
        "strokeColor": "#1e1e1e",
        "backgroundColor": "transparent",
        "fontSize": 20,
        "fontFamily": 1,
        "textAlign": "center",
        "verticalAlign": "top",
        "lineHeight": 1.25
    }
    args.update(kwargs)

    return {
        "type": "text",
        "version": 1,
        "isDeleted": False,
        "id": generate_id(),
        "fillStyle": args['fillStyle'],
        "strokeWidth": args['strokeWidth'],
        "strokeStyle": args['strokeStyle'],
        "roughness": args['roughness'],
        "opacity": args['opacity'],
        "angle": args['angle'],
        "x": x,
        "y": y,
        "strokeColor": args['strokeColor'],
        "backgroundColor": args['backgroundColor'],
        "text": text,
        "rawText": text,
        "isDeleted": False,
        "textAlign": args['textAlign'],
        "verticalAlign": args['verticalAlign'],
        "originalText": text,
        "lineHeight": args['lineHeight'],
    }
