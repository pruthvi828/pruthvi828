import os

OUTPUT_SVG = "info-card.svg"
STATIC = os.environ.get("STATIC", "0") == "1"

# Terminal colors
BG_COLOR = "#0d1117"
TEXT_COLOR = "#c9d1d9"
LABEL_COLOR = "#58a6ff"
TITLE_COLOR = "#39d353"

ANIMATION_DURATION = 0.3
DELAY_BETWEEN_LINES = 0.2

card_lines = [
    ("Role", "Hardware and Software Engineer"),
    ("Embedded", "Microcontrollers, Systems Design"),
    ("Hardware", "KiCad, PCB Routing, AutoCAD"),
    ("Software", "Software Development"),
    ("Status", "Building awesome tech!"),
]

title_line = "engineer@github"

svg_width = 490
svg_height = len(card_lines) * 25 + 100

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">
<style>
    .terminal-text {{
        font-family: 'Courier New', Courier, monospace;
        font-size: 14px;
        white-space: pre;
    }}
    .title {{ fill: {TITLE_COLOR}; font-weight: bold; }}
    .label {{ fill: {LABEL_COLOR}; font-weight: bold; }}
    .value {{ fill: {TEXT_COLOR}; }}
"""

if not STATIC:
    svg_content += """
    @keyframes fadeInSlide {
        0% { opacity: 0; transform: translateX(-10px); }
        100% { opacity: 1; transform: translateX(0); }
    }
    .fade-in {
        opacity: 0;
        animation: fadeInSlide """ + str(ANIMATION_DURATION) + """s ease-out forwards;
    }
"""

svg_content += f"""</style>
<rect width="100%" height="100%" fill="{BG_COLOR}" rx="8" />
<g transform="translate(20, 30)">
"""

# Title
delay = 0
fade_class = "fade-in" if not STATIC else ""
anim_style = f"style='animation-delay: {delay}s;'" if not STATIC else ""
svg_content += f"    <text class='terminal-text title {fade_class}' x='0' y='0' {anim_style}>{title_line}</text>\n"
svg_content += f"    <text class='terminal-text {fade_class}' x='0' y='10' {anim_style} fill='{TEXT_COLOR}'>-------------------</text>\n"

# Lines
for i, (label, value) in enumerate(card_lines):
    y_pos = 35 + (i * 25)
    delay += DELAY_BETWEEN_LINES
    anim_style = f"style='animation-delay: {delay}s;'" if not STATIC else ""
    svg_content += f"    <g class='{fade_class}' {anim_style}>\n"
    svg_content += f"        <text class='terminal-text label' x='0' y='{y_pos}'>{label}</text>\n"
    svg_content += f"        <text class='terminal-text value' x='100' y='{y_pos}'>: {value}</text>\n"
    svg_content += f"    </g>\n"

svg_content += """
</g>
</svg>
"""

with open(OUTPUT_SVG, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"Created {OUTPUT_SVG}")