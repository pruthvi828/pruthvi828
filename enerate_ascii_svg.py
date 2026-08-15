from PIL import Image
import numpy as np
import math

# 1. Configuration
INPUT_IMAGE = "photo.jpg"  # Replace with your photo path
OUTPUT_SVG = "animated_ascii.svg"
WIDTH_IN_CHARS = 80          # How wide the ASCII art should be
FONT_SIZE = 12
LINE_HEIGHT = 14
CHAR_ASPECT_RATIO = 0.55     # Fonts are usually twice as tall as they are wide
ANIMATION_DURATION = 0.1     # Seconds it takes to "type" a single line

# The ASCII ramp from bright (space) to dark (dense characters)
ASCII_RAMP = " .`:-=+*cs#%@" 

def get_character_for_pixel(brightness):
    # Brightness is 0 (black) to 255 (white)
    # We invert it so white backgrounds map to space (" ")
    index = math.floor((255 - brightness) / 255 * (len(ASCII_RAMP) - 1))
    return ASCII_RAMP[index]

def main():
    # 2. Load and process the image
    try:
        img = Image.open(INPUT_IMAGE).convert('L') # Convert to grayscale
    except FileNotFoundError:
        print(f"Error: Could not find '{INPUT_IMAGE}'. Please place an image with this name in the folder.")
        return

    # Calculate new height based on char aspect ratio to prevent squishing
    w, h = img.size
    aspect_ratio = h / w
    new_height = int(aspect_ratio * WIDTH_IN_CHARS * CHAR_ASPECT_RATIO)
    
    img = img.resize((WIDTH_IN_CHARS, new_height))
    pixels = np.array(img)

    # 3. Generate the ASCII lines
    ascii_lines = []
    for row in pixels:
        line = "".join([get_character_for_pixel(pixel) for pixel in row])
        # Replace spaces with non-breaking spaces so SVG preserves them
        line = line.replace(" ", "&#160;")
        ascii_lines.append(line)

    # 4. Calculate SVG dimensions
    svg_width = WIDTH_IN_CHARS * FONT_SIZE * 0.6 # Approximate char width
    svg_height = new_height * LINE_HEIGHT + 40   # Add some padding

    # 5. Build the SVG template with CSS animations
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">
    <style>
        .terminal-text {{
            font-family: 'Courier New', Courier, monospace;
            font-size: {FONT_SIZE}px;
            fill: #a8b2c1; /* A nice terminal gray */
            white-space: pre;
        }}
        
        /* The clipping animation that creates the typing effect */
        @keyframes typeLine {{
            from {{ clip-path: polygon(0 0, 0 0, 0 100%, 0 100%); }}
            to {{ clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%); }}
        }}

        .typing-line {{
            /* Start invisible (clipped to 0 width) */
            clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);
            /* Forwards ensures it stays visible after animation ends */
            animation: typeLine {ANIMATION_DURATION}s steps({WIDTH_IN_CHARS}, end) forwards;
        }}
    </style>
    
    <rect width="100%" height="100%" fill="#0d1117" /> <!-- GitHub Dark Mode background -->
    <g transform="translate(20, 20)">
    """

    # 6. Inject each line into the SVG with a staggered animation delay
    for i, line in enumerate(ascii_lines):
        y_pos = (i + 1) * LINE_HEIGHT
        delay = i * ANIMATION_DURATION # Stagger the start time
        svg_content += f'      <text class="terminal-text typing-line" x="0" y="{y_pos}" style="animation-delay: {delay}s;">{line}</text>\n'

    svg_content += """    </g>
</svg>"""

    # 7. Write to file
    with open(OUTPUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    print(f"Success! Created {OUTPUT_SVG}. Open it in your web browser to see the animation.")

if __name__ == "__main__":
    main()