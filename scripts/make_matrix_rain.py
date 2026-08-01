import random
import os

OUTPUT_SVG = "matrix-rain.svg"

SVG_WIDTH = 860
SVG_HEIGHT = 300

COLS = 50
ROWS = 15

CHAR_WIDTH = SVG_WIDTH / COLS
CHAR_HEIGHT = SVG_HEIGHT / ROWS

# Katakana and Latin characters used in Matrix
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$+-*/=%\"'#&_(),.;:?!\\|{}<>[]^~"
HIDDEN_WORD = "PRUTHVI"

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}" width="{SVG_WIDTH}" height="{SVG_HEIGHT}">
<style>
    .matrix-text {{
        font-family: 'Courier New', Courier, monospace;
        font-size: 16px;
        font-weight: bold;
        fill: #0F0;
        text-anchor: middle;
    }}
    .glow {{
        fill: #FFF;
        filter: drop-shadow(0px 0px 4px #0F0);
    }}
    .bg {{ fill: #000; }}
</style>
<rect width="100%" height="100%" class="bg" rx="10" />
"""

random.seed(42) # For reproducible output

# Place hidden word
hidden_col = random.randint(10, COLS - 10)
hidden_start_row = random.randint(2, ROWS - len(HIDDEN_WORD) - 2)

for col in range(COLS):
    x = col * CHAR_WIDTH + (CHAR_WIDTH / 2)
    
    # We create a column by adding a group with an animation
    delay = random.uniform(0, 5)
    duration = random.uniform(3, 8)
    
    svg_content += f'<g style="animation: fall_{col} {duration}s linear infinite; animation-delay: {delay}s; transform: translateY(-100%);">\n'
    
    # Generate CSS for this specific column to handle the falling animation
    svg_content += f"""<style>
    @keyframes fall_{col} {{
        0% {{ transform: translateY(-100%); }}
        100% {{ transform: translateY({SVG_HEIGHT}px); }}
    }}
    </style>\n"""

    for row in range(ROWS * 2): # Make it taller than screen for smooth falling
        y = row * CHAR_HEIGHT
        
        # Check if we should insert the hidden word here
        is_hidden = False
        if col == hidden_col and hidden_start_row <= row < hidden_start_row + len(HIDDEN_WORD):
            char = HIDDEN_WORD[row - hidden_start_row]
            is_hidden = True
        else:
            char = random.choice(CHARS)
            
        # The lowest character in the column is brightest (head of the drop)
        is_head = row == ROWS * 2 - 1
        
        classes = "matrix-text"
        if is_head or is_hidden:
            classes += " glow"
            
        # Random opacity fade trailing upwards
        opacity = 1.0 - ( (ROWS * 2 - 1 - row) / (ROWS * 2) )
        if is_hidden:
            opacity = 1.0
            
        # SVG expects literal text inside tags, XML escape if needed (handled by choosing safe chars mostly, but avoid <, > if possible, actually let's sanitize)
        safe_char = char
        if char == '<': safe_char = '&lt;'
        if char == '>': safe_char = '&gt;'
        if char == '&': safe_char = '&amp;'
        
        svg_content += f'  <text x="{x}" y="{y}" class="{classes}" opacity="{opacity:.2f}">{safe_char}</text>\n'
    
    svg_content += '</g>\n'

svg_content += "</svg>"

with open(OUTPUT_SVG, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"Created {OUTPUT_SVG}")
