import os

OUTPUT_SVG = "header-banner.svg"

# Cyberpunk Colors
BG_START = "#140a25" # Deep purple
BG_END = "#06060c"   # Almost black
NEON_CYAN = "#00f0ff"
NEON_PINK = "#ff003c"
GRID_COLOR = "#2a1b41"

svg_width = 860
svg_height = 200

# Generate a grid pattern
grid_lines = ""
for x in range(0, svg_width, 40):
    grid_lines += f'<line x1="{x}" y1="0" x2="{x}" y2="{svg_height}" class="grid-line" />\n'
for y in range(0, svg_height, 40):
    grid_lines += f'<line x1="0" y1="{y}" x2="{svg_width}" y2="{y}" class="grid-line" />\n'

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">
<defs>
    <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="{BG_START}" />
        <stop offset="100%" stop-color="{BG_END}" />
    </linearGradient>
    
    <!-- Glow Filters -->
    <filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="5" result="blur" />
        <feMerge>
            <feMergeNode in="blur" />
            <feMergeNode in="SourceGraphic" />
        </feMerge>
    </filter>
    <filter id="glow-pink" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="5" result="blur" />
        <feMerge>
            <feMergeNode in="blur" />
            <feMergeNode in="SourceGraphic" />
        </feMerge>
    </filter>
</defs>

<style>
    .bg {{ fill: url(#bgGradient); }}
    .grid-line {{ stroke: {GRID_COLOR}; stroke-width: 1; opacity: 0.5; }}
    
    .title-text {{
        font-family: 'Arial Black', Impact, sans-serif;
        font-size: 56px;
        fill: #ffffff;
        letter-spacing: 4px;
        font-style: italic;
    }}
    .subtitle-text {{
        font-family: 'Courier New', Courier, monospace;
        font-size: 16px;
        fill: {NEON_CYAN};
        letter-spacing: 2px;
    }}
    
    .node-pink {{
        fill: {NEON_PINK};
        filter: url(#glow-pink);
        animation: pulse 2s infinite alternate;
    }}
    .node-cyan {{
        fill: {NEON_CYAN};
        filter: url(#glow-cyan);
        animation: pulse 3s infinite alternate-reverse;
    }}
    
    .data-line {{
        stroke: {NEON_CYAN};
        stroke-width: 2;
        fill: none;
        stroke-dasharray: 20 80;
        animation: slide 4s linear infinite;
    }}

    @keyframes pulse {{
        0% {{ opacity: 0.3; r: 2; }}
        100% {{ opacity: 1.0; r: 6; }}
    }}
    
    @keyframes slide {{
        0% {{ stroke-dashoffset: 100; }}
        100% {{ stroke-dashoffset: 0; }}
    }}
    
    @keyframes float {{
        0% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-8px); }}
        100% {{ transform: translateY(0px); }}
    }}
</style>

<!-- Background & Grid -->
<rect width="100%" height="100%" class="bg" rx="10" />
{grid_lines}

<!-- Animated Data Lines -->
<path class="data-line" d="M 0,50 L 200,50 L 250,100 L 860,100" />
<path class="data-line" d="M 860,150 L 650,150 L 600,80 L 0,80" style="animation-duration: 6s;" />

<!-- Glowing Nodes -->
<circle cx="200" cy="50" r="4" class="node-pink" />
<circle cx="250" cy="100" r="4" class="node-cyan" />
<circle cx="650" cy="150" r="4" class="node-pink" style="animation-delay: 1s;" />
<circle cx="600" cy="80" r="4" class="node-cyan" style="animation-delay: 1s;" />

<!-- Text Content (Floating) -->
<g style="animation: float 6s ease-in-out infinite;">
    <!-- Cyberpunk Glitch Effect Text (Cyan layer offset behind White) -->
    <text x="430" y="110" class="title-text" text-anchor="middle" fill="{NEON_CYAN}" style="opacity:0.8; transform: translate(3px, 3px);">PRUTHVI</text>
    <text x="430" y="110" class="title-text" text-anchor="middle">PRUTHVI</text>
    
    <text x="430" y="145" class="subtitle-text" text-anchor="middle">/// HARDWARE and SOFTWARE ENGINEER</text>
</g>

<!-- Accent blocks -->
<rect x="40" y="40" width="30" height="10" fill="{NEON_PINK}" opacity="0.8" />
<rect x="790" y="150" width="30" height="10" fill="{NEON_CYAN}" opacity="0.8" />

</svg>
"""

with open(OUTPUT_SVG, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"Created {OUTPUT_SVG}")
