import os
import random
import math
import numpy as np
from PIL import Image, ImageOps, ImageFilter
from scipy.optimize import linear_sum_assignment

def get_logo_points(logo_id, num_points):
    """Generate points for a simple shape representing a logo."""
    points = []
    cx, cy = 950, 300 # Center of right panel
    r = 100
    if logo_id == 0: # Circle
        for i in range(num_points):
            angle = (i / num_points) * 2 * math.pi
            points.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    elif logo_id == 1: # Square
        side = int(num_points / 4)
        for i in range(num_points):
            pos = i / num_points
            if pos < 0.25:
                p = (pos/0.25)
                points.append((cx - r + p*2*r, cy - r))
            elif pos < 0.5:
                p = (pos-0.25)/0.25
                points.append((cx + r, cy - r + p*2*r))
            elif pos < 0.75:
                p = (pos-0.5)/0.25
                points.append((cx + r - p*2*r, cy + r))
            else:
                p = (pos-0.75)/0.25
                points.append((cx - r, cy + r - p*2*r))
    else: # ESP32
        for i in range(num_points):
            pos = i / num_points
            if pos < 0.4:
                p = pos / 0.4
                hw, hh = 50, 70
                if p < 0.25: points.append((cx - hw + (p/0.25)*2*hw, cy - hh))
                elif p < 0.5: points.append((cx + hw, cy - hh + ((p-0.25)/0.25)*2*hh))
                elif p < 0.75: points.append((cx + hw - ((p-0.5)/0.25)*2*hw, cy + hh))
                else: points.append((cx - hw, cy + hh - ((p-0.75)/0.25)*2*hh))
            elif pos < 0.7:
                p = (pos - 0.4) / 0.3
                hw, hh = 35, 45
                sy = cy + 15
                if p < 0.25: points.append((cx - hw + (p/0.25)*2*hw, sy - hh))
                elif p < 0.5: points.append((cx + hw, sy - hh + ((p-0.25)/0.25)*2*hh))
                elif p < 0.75: points.append((cx + hw - ((p-0.5)/0.25)*2*hw, sy + hh))
                else: points.append((cx - hw, sy + hh - ((p-0.75)/0.25)*2*hh))
            else:
                p = (pos - 0.7) / 0.3
                x = cx - 35 + p * 70
                y = cy - 65 + (15 if int(p * 12) % 2 == 0 else 0)
                points.append((x, y))
    return np.array(points)

def floyd_steinberg_dither(img_array):
    h, w = img_array.shape
    dithered = np.copy(img_array)
    dots = []
    for y in range(h):
        for x in range(w):
            old_val = dithered[y, x]
            new_val = 255 if old_val > 128 else 0
            dithered[y, x] = new_val
            err = old_val - new_val
            if new_val == 0: # Dark mode -> keep dark parts (which are 0)
                dots.append((x, y))
            if x + 1 < w:
                dithered[y, x + 1] = min(max(dithered[y, x + 1] + err * 7 / 16, 0), 255)
            if y + 1 < h:
                if x > 0:
                    dithered[y + 1, x - 1] = min(max(dithered[y + 1, x - 1] + err * 3 / 16, 0), 255)
                dithered[y + 1, x] = min(max(dithered[y + 1, x] + err * 5 / 16, 0), 255)
                if x + 1 < w:
                    dithered[y + 1, x + 1] = min(max(dithered[y + 1, x + 1] + err * 1 / 16, 0), 255)
    return dots

def build_banner():
    # Load and process image
    img_path = "photo1.png"
    if not os.path.exists(img_path):
        img = Image.new('L', (300, 340), color=255)
    else:
        img = Image.open(img_path).convert('L')
    
    # Resize and crop to 300x340
    img = ImageOps.fit(img, (300, 340), Image.Resampling.LANCZOS)
    
    # Remove background using rembg
    try:
        from rembg import remove
        img = remove(img)
        # Extract alpha mask
        if img.mode == 'RGBA':
            r, g, b, a = img.split()
            mask = a
            # Create a solid black background
            bg = Image.new('RGB', img.size, (0, 0, 0))
            bg.paste(img, mask=mask)
            img = bg.convert('L')
        else:
            img = img.convert('L')
            mask = Image.new('L', img.size, 255)
    except ImportError:
        img = img.convert('L')
        mask = Image.new('L', img.size, 255)
    
    img = ImageOps.autocontrast(img, cutoff=1)
    img = img.filter(ImageFilter.UnsharpMask(radius=3, percent=140))
    
    # Invert the image so that bright parts of the face get more dots in dark mode
    img = ImageOps.invert(img)
    
    img_array = np.array(img, dtype=float)
    mask_array = np.array(mask, dtype=float)
    
    # Apply dither
    dithered_dots = floyd_steinberg_dither(img_array)
    
    # Filter dots using the mask (only keep dots inside the subject)
    portrait_dots = [(x, y) for x, y in dithered_dots if mask_array[y, x] > 128]
    
    # Subsample dots to prevent file size blowup
    portrait_dots = random.sample(portrait_dots, min(len(portrait_dots), 12000))
    
    # Travellers
    num_travellers = 500
    l1 = get_logo_points(0, num_travellers)
    l2 = get_logo_points(1, num_travellers)
    l3 = get_logo_points(2, num_travellers)
    
    # Match using linear sum assignment
    cost12 = np.linalg.norm(l1[:, None] - l2, axis=2)
    _, cols12 = linear_sum_assignment(cost12)
    l2_matched = l2[cols12]
    
    cost23 = np.linalg.norm(l2_matched[:, None] - l3, axis=2)
    _, cols23 = linear_sum_assignment(cost23)
    l3_matched = l3[cols23]

    svg_content = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 610" width="1180" height="610">',
        '<style>',
        '  .bg { fill: #0A101F; }',
        '  .dot { fill: #A78BFA; shape-rendering: crispEdges; }',
        '  .traveller { fill: #22D3EE; shape-rendering: crispEdges; }',
        '  .text-main { fill: #22D3EE; font-family: monospace; font-size: 14px; }',
        '  .text-label { fill: #10B981; font-family: monospace; font-size: 14px; }',
        '</style>',
        '<rect width="100%" height="100%" class="bg" rx="15" />',
        '<!-- SYSTEM.INFO Text -->'
        '<text x="500" y="50" class="text-label">SYSTEM.INFO</text>',
        '<text x="500" y="80" class="text-main">Subject: Pruthvi</text>',
        '<text x="500" y="110" class="text-main">Role: Hardware &amp; Software Engineer</text>',
        '<text x="500" y="140" class="text-main">Location: Earth</text>',
        '<text x="500" y="170" class="text-main">Education: Engineering</text>',
        '<text x="500" y="200" class="text-main">Status: Building + Learning + Shipping</text>',
        '<text x="500" y="230" class="text-main">ToolChain: Kicad, AutoCAD, VS Code, Git</text>',
        '<text x="500" y="260" class="text-main">Core.Lang: C, C++, Python</text>',
        '<g transform="translate(50, 100)">'
    ]

    # Portrait dots
    for x, y in portrait_dots:
        d_val = random.randint(0, 20)
        svg_content.append(f'<rect x="{x}" y="{y}" width="2" height="2" class="dot"><animate attributeName="opacity" values="0;1;1" keyTimes="0;0.1;1" begin="{d_val/10}s" dur="14.2s" repeatCount="indefinite" /></rect>')
        
    svg_content.append('</g>')

    # Travellers
    for i in range(num_travellers):
        p1 = l1[i]
        p2 = l2_matched[i]
        p3 = l3_matched[i]
        
        # Opacity hidden during portrait phase (first 3s of 14.2s loop)
        path = f'M {p1[0]},{p1[1]} L {p2[0]},{p2[1]} L {p3[0]},{p3[1]} L {p1[0]},{p1[1]}'
        svg_content.append(f'<rect width="2" height="2" class="traveller"><animateMotion path="{path}" dur="14.2s" repeatCount="indefinite" keyPoints="0;0.2;0.5;0.7;1" keyTimes="0;0.21;0.5;0.71;1" calcMode="linear" /><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.21;0.22;0.99;1" dur="14.2s" repeatCount="indefinite" /></rect>')

    svg_content.append('</svg>')
    
    with open("dark.svg", "w") as f:
        f.write("".join(svg_content))
    print("Created dark.svg")

if __name__ == "__main__":
    build_banner()
