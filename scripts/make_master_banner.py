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
        img = Image.new('L', (430, 490), color=128)
        mask = Image.new('L', (430, 490), 255)
    else:
        raw = Image.open(img_path)
        
        # Use built-in alpha channel as mask if available (transparent background PNG)
        if raw.mode == 'RGBA':
            r, g, b, a = raw.split()
            mask = a.resize((430, 490), Image.Resampling.LANCZOS)
            img = raw.convert('L')
        else:
            img = raw.convert('L')
            mask = Image.new('L', img.size, 255)

        # Try rembg as a fallback to improve mask
        try:
            from rembg import remove
            rgba = remove(raw)
            if rgba.mode == 'RGBA':
                _, _, _, a2 = rgba.split()
                mask = a2
        except Exception:
            pass  # Keep the alpha mask from above or full white mask
    
    # Resize and crop to 430x490 for a larger portrait
    img = ImageOps.fit(img, (430, 490), Image.Resampling.LANCZOS)
    mask = ImageOps.fit(mask, (430, 490), Image.Resampling.LANCZOS)
    
    img = ImageOps.autocontrast(img, cutoff=2)
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=180))
    
    # Invert so dark face features (hair, eyes, shadows) become the dot art pattern
    img = ImageOps.invert(img)
    
    img_array = np.array(img, dtype=float)
    mask_array = np.array(mask, dtype=float)
    
    # Apply dither
    dithered_dots = floyd_steinberg_dither(img_array)
    
    # Filter dots using the mask (only keep dots inside the subject)
    portrait_dots = [(x, y) for x, y in dithered_dots if mask_array[y, x] > 128]
    
    # Subsample dots to prevent file size blowup
    portrait_dots = random.sample(portrait_dots, min(len(portrait_dots), 18000))
    
    # Travellers removed

    # Also store original pixel brightness for dot color variation
    raw_array = np.array(img, dtype=float)  # already inverted: bright = more dots

    svg_content = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 620" width="1180" height="620">',
        '<defs>',
        '  <filter id="glow"><feGaussianBlur stdDeviation="3" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
        '  <linearGradient id="divGrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#22D3EE" stop-opacity="0"/><stop offset="30%" stop-color="#22D3EE" stop-opacity="1"/><stop offset="70%" stop-color="#A78BFA" stop-opacity="1"/><stop offset="100%" stop-color="#A78BFA" stop-opacity="0"/></linearGradient>',
        '</defs>',
        '<style>',
        '  .bg { fill: #080E1C; }',
        '  .text-main { fill: #E2E8F0; font-family: "Courier New", monospace; font-size: 18px; }',
        '  .text-label { fill: #22D3EE; font-family: "Courier New", monospace; font-size: 13px; letter-spacing: 3px; }',
        '  .text-value { fill: #A78BFA; font-family: "Courier New", monospace; font-size: 18px; font-weight: bold; }',
        '  .text-key { fill: #10B981; font-family: "Courier New", monospace; font-size: 18px; }',
        '  .corner { fill: none; stroke: #22D3EE; stroke-width: 2; opacity: 0.7; }',
        '  .scanline { fill: #22D3EE; opacity: 0.03; }',
        '</style>',
        # Background
        '<rect width="100%" height="100%" class="bg" rx="12" />',
        # Top terminal bar
        '<rect x="0" y="0" width="1180" height="36" fill="#0F172A" rx="12"/>',
        '<rect x="0" y="24" width="1180" height="12" fill="#0F172A"/>',
        '<circle cx="22" cy="18" r="6" fill="#FF5F57"/>',
        '<circle cx="44" cy="18" r="6" fill="#FFBD2E"/>',
        '<circle cx="66" cy="18" r="6" fill="#28C840"/>',
        '<text x="590" y="23" text-anchor="middle" class="text-label" font-size="11px">PRUTHVI@GITHUB:~/profile</text>',
        # Corner decorations (top-left portrait area)
        '<rect x="20" y="48" width="20" height="3" class="corner"/>',
        '<rect x="20" y="48" width="3" height="20" class="corner"/>',
        '<rect x="440" y="48" width="20" height="3" class="corner"/>',
        '<rect x="457" y="48" width="3" height="20" class="corner"/>',
        '<rect x="20" y="582" width="20" height="3" class="corner"/>',
        '<rect x="20" y="565" width="3" height="20" class="corner"/>',
        '<rect x="440" y="582" width="20" height="3" class="corner"/>',
        '<rect x="457" y="565" width="3" height="20" class="corner"/>',
        # Glowing vertical divider
        '<rect x="476" y="44" width="2" height="540" fill="url(#divGrad)" filter="url(#glow)"/>',
        # System info panel
        '<text x="510" y="90"  class="text-label">SYSTEM.INFO</text>',
        '<line x1="510" y1="97" x2="830" y2="97" stroke="#22D3EE" stroke-width="1" opacity="0.4"/>',
        '<text x="510" y="135"><tspan class="text-key">Subject  </tspan><tspan class="text-main"> : </tspan><tspan class="text-value">Pruthvi</tspan></text>',
        '<text x="510" y="175"><tspan class="text-key">Role     </tspan><tspan class="text-main"> : </tspan><tspan class="text-value">Hardware &amp; Software Eng.</tspan></text>',
        '<text x="510" y="215"><tspan class="text-key">Location </tspan><tspan class="text-main"> : </tspan><tspan class="text-value">Earth</tspan></text>',
        '<text x="510" y="255"><tspan class="text-key">Education</tspan><tspan class="text-main"> : </tspan><tspan class="text-value">Engineering</tspan></text>',
        '<text x="510" y="295"><tspan class="text-key">Status   </tspan><tspan class="text-main"> : </tspan><tspan class="text-value">Building + Learning</tspan></text>',
        '<text x="510" y="335"><tspan class="text-key">ToolChain</tspan><tspan class="text-main"> : </tspan><tspan class="text-value">Kicad, AutoCAD, Git</tspan></text>',
        '<text x="510" y="375"><tspan class="text-key">Core.Lang</tspan><tspan class="text-main"> : </tspan><tspan class="text-value">C, C++, Python</tspan></text>',
        # Blinking cursor
        '<rect x="510" y="400" width="12" height="20" fill="#22D3EE"><animate attributeName="opacity" values="1;0;1" dur="1.2s" repeatCount="indefinite"/></rect>',
        # Portrait group
        '<g transform="translate(28, 52)">',
    ]

    # Portrait dots with color variation based on intensity
    dot_colors = ['#6D28D9', '#7C3AED', '#8B5CF6', '#A78BFA', '#C4B5FD', '#DDD6FE']
    for x, y in portrait_dots:
        # Get pixel brightness (0=dark=dense dots, 255=bright)
        bx, by = min(int(x), raw_array.shape[1]-1), min(int(y), raw_array.shape[0]-1)
        brightness = raw_array[by, bx]
        # Map brightness to color: darker original (after invert = high val) = brighter dot
        color_idx = min(int(brightness / 255 * (len(dot_colors)-1)), len(dot_colors)-1)
        color = dot_colors[color_idx]
        delay = random.uniform(0, 8)
        dur = random.uniform(1.5, 4.0)
        svg_content.append(
            f'<rect x="{x}" y="{y}" width="3" height="3" fill="{color}" shape-rendering="crispEdges">'
            f'<animate attributeName="opacity" values="0.2;1;0.2" '
            f'keyTimes="0;0.5;1" begin="{delay:.2f}s" dur="{dur:.2f}s" '
            f'repeatCount="indefinite" calcMode="spline" '
            f'keySplines="0.4 0 0.6 1;0.4 0 0.6 1" /></rect>'
        )
        
    svg_content.append('</g>')
    svg_content.append('</svg>')

    with open("dark.svg", "w") as f:
        f.write("".join(svg_content))
    print("Created dark.svg")
if __name__ == "__main__":
    build_banner()
