"""
Excalidraw element types taken from /packages/tests/helpers/api.ts createElement function
base =
- id
- width
- height
- type
- seed
- version
- versionNonce
- isDeleted
- groupIds
- link
- updated
    - x
    - y
    - frameId = null
    - angle = 0
    - strokeColor
    - backgroundColor
    - fillStyle
    - strokeWidth
    - strokeStyle
    - roundness = "round"
    - roughness
    - opacity
    - boundElements = null

1. [rectangle, diamond, ellipse]
    type = "rectangle" | "diamond" | "ellipse"
    width
    height
2. embeddable
    type = "embeddable"
3. iframe
    type = "iframe"
4. text
    type = "text"
    fontSize
    fontFamily
    textAlign
    verticalAlign = "top"
    containerId = undefined
    width
    height
5. freedraw
    type = "freedraw"
    simulatePressure = true
6. [arrow, line]
    width
    height
    type = "arrow" | "line"
    startArrowHead
    endArrowHead
    points = [
        [0, 0],
        [100, 100]
    ]
    if arrow:
        startBinding
        endBinding
7. image
    width
    height
    type = "image"
    fileId
    status = "saved"
    scale = [1, 1]
8. [frame, magicelement]
    width
    height
"""