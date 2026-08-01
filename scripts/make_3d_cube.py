import math
import os

OUTPUT_SVG = "3d-cube.svg"

# Cube vertices
vertices = [
    [-1, -1, -1], [ 1, -1, -1], [ 1,  1, -1], [-1,  1, -1],
    [-1, -1,  1], [ 1, -1,  1], [ 1,  1,  1], [-1,  1,  1]
]

# Cube edges (pairs of vertex indices)
edges = [
    (0,1), (1,2), (2,3), (3,0),
    (4,5), (5,6), (6,7), (7,4),
    (0,4), (1,5), (2,6), (3,7)
]

FRAMES = 60
SVG_WIDTH = 400
SVG_HEIGHT = 400
SCALE = 100

def project(x, y, z):
    # Simple orthographic projection
    # Offset to center
    return (x * SCALE + SVG_WIDTH / 2, y * SCALE + SVG_HEIGHT / 2)

def rotate(v, ax, ay, az):
    x, y, z = v
    # Rotate X
    x1 = x
    y1 = y * math.cos(ax) - z * math.sin(ax)
    z1 = y * math.sin(ax) + z * math.cos(ax)
    
    # Rotate Y
    x2 = x1 * math.cos(ay) + z1 * math.sin(ay)
    y2 = y1
    z2 = -x1 * math.sin(ay) + z1 * math.cos(ay)
    
    # Rotate Z
    x3 = x2 * math.cos(az) - y2 * math.sin(az)
    y3 = x2 * math.sin(az) + y2 * math.cos(az)
    z3 = z2
    
    return [x3, y3, z3]

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}" width="{SVG_WIDTH}" height="{SVG_HEIGHT}">
<style>
    .edge {{
        stroke: #39d353;
        stroke-width: 3;
        fill: none;
        stroke-linecap: round;
        stroke-linejoin: round;
    }}
</style>
<rect width="100%" height="100%" fill="#0d1117" rx="8" />
"""

# Generate paths for each edge across all frames
for edge_idx, edge in enumerate(edges):
    v1_idx, v2_idx = edge
    
    path_data_frames = []
    
    for frame in range(FRAMES):
        # Calculate rotation angles (full 360 degree rotation over FRAMES)
        angle = (frame / FRAMES) * 2 * math.pi
        
        # We rotate on X and Y axes to make it look 3D
        rot_x = angle
        rot_y = angle * 1.5
        
        v1 = rotate(vertices[v1_idx], rot_x, rot_y, 0)
        v2 = rotate(vertices[v2_idx], rot_x, rot_y, 0)
        
        p1 = project(v1[0], v1[1], v1[2])
        p2 = project(v2[0], v2[1], v2[2])
        
        d = f"M {p1[0]:.1f},{p1[1]:.1f} L {p2[0]:.1f},{p2[1]:.1f}"
        path_data_frames.append(d)
    
    # Repeat the first frame at the end for a perfect loop
    path_data_frames.append(path_data_frames[0])
    
    values_str = ";".join(path_data_frames)
    
    svg_content += f"""
<path class="edge" d="{path_data_frames[0]}">
    <animate attributeName="d" values="{values_str}" dur="5s" repeatCount="indefinite" />
</path>
"""

svg_content += "</svg>"

with open(OUTPUT_SVG, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"Created {OUTPUT_SVG}")
