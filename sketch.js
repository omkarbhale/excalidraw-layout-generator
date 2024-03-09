// Set up local p5.js environment or run on https://editor.p5js.org/
// Force directed layout based on https://cs.brown.edu/people/rtamassi/gdhandbook/chapters/force-directed.pdf

// If you wish to test nodes without any edges
// const nodes = {
//   'A': {edges: [], position: null, fill: null, forces: null},
//   'B': {edges: [], position: null, fill: null, forces: null},
//   'C': {edges: [], position: null, fill: null, forces: null},
//   'D': {edges: [], position: null, fill: null, forces: null},
//   'E': {edges: [], position: null, fill: null, forces: null}
// };
const nodes = {
    'A': { edges: ['B', 'C', 'E'], position: null, fill: null, forces: null },
    'B': { edges: [], position: null, fill: null, forces: null },
    'C': { edges: [], position: null, fill: null, forces: null },
    'D': { edges: ['E'], position: null, fill: null, forces: null },
    'E': { edges: [], position: null, fill: null, forces: null }
};

function setup() {
    createCanvas(600, 600);
    for (let id in nodes) {
        nodes[id].position = {
            x: Math.floor(random(50, 550)),
            y: Math.floor(random(50, 550)),
        };
        nodes[id].fill = [random(255), random(255), random(255)];
    }
}

function draw() {
    background(50);

    // Adjust parameters to your liking
    const c1 = 30; // How fast strings snap
    const c2 = 150; // Ideal distance between adjacent nodes
    const c3 = 2000; // Force between non-adjacent nodes
    const c4 = 0.4; // Overall delta-displacement based on forces

    // Calculate forces
    for (const id in nodes) { nodes[id].forces = [] } // Empty forces
    for (const id in nodes) {
        // Spring force for edges
        for (const edge of nodes[id].edges) {
            const d = dist(
                nodes[id].position.x, nodes[id].position.y,
                nodes[edge].position.x, nodes[edge].position.y
            );
            const forceMag = c1 * log(d / c2);
            const forceAngle = {
                x: (nodes[edge].position.x - nodes[id].position.x) / d,
                y: (nodes[edge].position.y - nodes[id].position.y) / d
            }
            nodes[id].forces.push({ magnitude: forceMag, angle: forceAngle, other: edge });
            nodes[edge].forces.push({ magnitude: -forceMag, angle: forceAngle, other: id })
        }

        // Inverse square forces on all other nodes
        for (const otherid in nodes) {
            // If current node or edge ignore
            if (id === otherid || nodes[id].edges.includes(otherid) || nodes[otherid].edges.includes[id]) continue;

            const d = dist(
                nodes[id].position.x, nodes[id].position.y,
                nodes[otherid].position.x, nodes[otherid].position.y
            );
            const forceMag = c3 / Math.pow(d, 1.6);
            const forceAngle = {
                x: (nodes[id].position.x - nodes[otherid].position.x) / d,
                y: (nodes[id].position.y - nodes[otherid].position.y) / d
            }
            nodes[id].forces.push({ magnitude: forceMag, angle: forceAngle, other: otherid });
        }
    }

    // Apply forces
    for (const id in nodes) {
        for (const force of nodes[id].forces) {
            nodes[id].position.x += c4 * force.magnitude * force.angle.x;
            nodes[id].position.y += c4 * force.magnitude * force.angle.y * 1.5;
        }
    }

    // Draw graph
    for (const id in nodes) {
        stroke(255);
        for (let edge of nodes[id].edges) {
            line(
                nodes[id].position.x, nodes[id].position.y,
                nodes[edge].position.x, nodes[edge].position.y
            );
        }

        noStroke();
        fill(...nodes[id].fill)
        circle(nodes[id].position.x, nodes[id].position.y, 32);
        noStroke(255);
        fill(255);
        text(id, nodes[id].position.x, nodes[id].position.y);
    }

    // Only iterate 100 times
    if (frameCount == 150) noLoop();
}