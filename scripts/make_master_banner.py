import os
import random
import numpy as np
from PIL import Image, ImageOps, ImageFilter

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
            if new_val == 0:
                dots.append((x, y))
            if x + 1 < w:
                dithered[y, x+1] = min(max(dithered[y, x+1] + err * 7/16, 0), 255)
            if y + 1 < h:
                if x > 0:
                    dithered[y+1, x-1] = min(max(dithered[y+1, x-1] + err * 3/16, 0), 255)
                dithered[y+1, x] = min(max(dithered[y+1, x] + err * 5/16, 0), 255)
                if x + 1 < w:
                    dithered[y+1, x+1] = min(max(dithered[y+1, x+1] + err * 1/16, 0), 255)
    return dots

def build_banner():
    img_path = "photo1.png"

    # Load image and extract alpha mask if RGBA
    if not os.path.exists(img_path):
        img = Image.new('L', (400, 500), color=128)
        mask = Image.new('L', (400, 500), 255)
    else:
        raw = Image.open(img_path)
        if raw.mode == 'RGBA':
            r, g, b, a = raw.split()
            mask = a
            img = raw.convert('L')
        else:
            img = raw.convert('L')
            mask = Image.new('L', img.size, 255)

    # Resize portrait to a good size
    TARGET_W, TARGET_H = 400, 500
    img  = ImageOps.fit(img,  (TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    mask = ImageOps.fit(mask, (TARGET_W, TARGET_H), Image.Resampling.LANCZOS)

    # Enhance contrast and sharpen
    img = ImageOps.autocontrast(img, cutoff=2)
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150))

    # Invert so dark areas (shadows/hair) produce dots on dark background
    img = ImageOps.invert(img)

    img_array  = np.array(img,  dtype=float)
    mask_array = np.array(mask, dtype=float)

    # Dither and filter by mask
    dithered_dots = floyd_steinberg_dither(img_array)
    portrait_dots = [(x, y) for x, y in dithered_dots if mask_array[y, x] > 128]
    portrait_dots = random.sample(portrait_dots, min(len(portrait_dots), 6000))

    # SVG dimensions
    SVG_W, SVG_H = 900, 560

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SVG_W} {SVG_H}" width="{SVG_W}" height="{SVG_H}">',
        '<style>',
        '  .bg   { fill: #0D1117; }',
        '  .dot  { fill: #A78BFA; shape-rendering: crispEdges; }',
        '  .lbl  { fill: #22D3EE; font-family: monospace; font-size: 12px; letter-spacing: 2px; }',
        '  .key  { fill: #10B981; font-family: monospace; font-size: 17px; }',
        '  .val  { fill: #C4B5FD; font-family: monospace; font-size: 17px; font-weight: bold; }',
        '  .sep  { fill: none; stroke: #22D3EE; stroke-width: 1.5; opacity: 0.5; }',
        '</style>',

        # Background
        f'<rect width="{SVG_W}" height="{SVG_H}" class="bg" rx="10"/>',

        # Vertical divider
        '<line x1="440" y1="20" x2="440" y2="540" class="sep"/>',

        # Info panel header
        '<text x="470" y="65" class="lbl">SYSTEM.INFO</text>',
        '<line x1="470" y1="72" x2="870" y2="72" stroke="#22D3EE" stroke-width="1" opacity="0.3"/>',

        # Info rows
        '<text x="470" y="110"><tspan class="key">Subject   </tspan><tspan class="val"> Pruthvi</tspan></text>',
        '<text x="470" y="150"><tspan class="key">Role      </tspan><tspan class="val"> HW &amp; SW Engineer</tspan></text>',
        '<text x="470" y="190"><tspan class="key">Location  </tspan><tspan class="val"> Earth</tspan></text>',
        '<text x="470" y="230"><tspan class="key">Education </tspan><tspan class="val"> Engineering</tspan></text>',
        '<text x="470" y="270"><tspan class="key">Status    </tspan><tspan class="val"> Building &amp; Learning</tspan></text>',
        '<text x="470" y="310"><tspan class="key">ToolChain </tspan><tspan class="val"> KiCad · AutoCAD · Git</tspan></text>',
        '<text x="470" y="350"><tspan class="key">Core.Lang </tspan><tspan class="val"> C · C++ · Python</tspan></text>',

        # Blinking cursor
        '<rect x="470" y="370" width="10" height="18" fill="#22D3EE">'
        '<animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/></rect>',

        # Portrait group (offset to center in left half)
        '<g transform="translate(20, 30)">',
    ]

    # Dots with continuous twinkling
    for x, y in portrait_dots:
        delay = random.uniform(0, 8)
        dur   = random.uniform(1.5, 4.0)
        lines.append(
            f'<rect x="{x}" y="{y}" width="2" height="2" class="dot">'
            f'<animate attributeName="opacity" values="0.2;1;0.2" '
            f'keyTimes="0;0.5;1" begin="{delay:.2f}s" dur="{dur:.2f}s" '
            f'repeatCount="indefinite" calcMode="spline" '
            f'keySplines="0.4 0 0.6 1;0.4 0 0.6 1"/></rect>'
        )

    lines.append('</g>')
    lines.append('</svg>')

    with open("dark.svg", "w") as f:
        f.write("".join(lines))
    print("Created dark.svg")

if __name__ == "__main__":
    build_banner()
