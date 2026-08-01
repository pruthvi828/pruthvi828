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
    
    # Travellers removed

    svg_content = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 610" width="1180" height="610">',
        '<style>',
        '  .bg { fill: #0A101F; }',
        '  .dot { fill: #A78BFA; shape-rendering: crispEdges; }',
        '  .traveller { fill: #22D3EE; shape-rendering: crispEdges; }',
        '  .text-main { fill: #22D3EE; font-family: monospace; font-size: 20px; font-weight: bold; letter-spacing: 0.5px; }',
        '  .text-label { fill: #10B981; font-family: monospace; font-size: 20px; font-weight: bold; letter-spacing: 2px; }',
        '</style>',
        '<rect width="100%" height="100%" class="bg" rx="15" />',
        '<text x="490" y="55"  class="text-label">SYSTEM.INFO</text>'
        '<text x="490" y="95"  class="text-main">Subject&#160;&#160;: Pruthvi</text>',
        '<text x="490" y="135" class="text-main">Role&#160;&#160;&#160;&#160;&#160;: Hardware &amp; Software Engineer</text>',
        '<text x="490" y="175" class="text-main">Location : Earth</text>',
        '<text x="490" y="215" class="text-main">Education: Engineering</text>',
        '<text x="490" y="255" class="text-main">Status&#160;&#160;&#160;: Building + Learning + Shipping</text>',
        '<text x="490" y="295" class="text-main">ToolChain: Kicad, AutoCAD, VS Code, Git</text>',
        '<text x="490" y="335" class="text-main">Core.Lang: C, C++, Python</text>',
        '<g transform="translate(50, 100)">'
    ]

    # Portrait dots
    for x, y in portrait_dots:
        d_val = random.randint(0, 20)
        svg_content.append(f'<rect x="{x}" y="{y}" width="2" height="2" class="dot"><animate attributeName="opacity" values="0;1;1" keyTimes="0;0.1;1" begin="{d_val/10}s" dur="14.2s" repeatCount="indefinite" /></rect>')
        
    svg_content.append('</g>')

    # Travellers removed

    svg_content.append('</svg>')
    
    with open("dark.svg", "w") as f:
        f.write("".join(svg_content))
    print("Created dark.svg")

if __name__ == "__main__":
    build_banner()
