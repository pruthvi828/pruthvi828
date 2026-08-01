import json
import os
import math

INPUT_JSON = os.path.join("data", "contributions.json")
OUTPUT_SVG = "contrib-heatmap.svg"

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

BOX_SIZE = 10
BOX_SPACING = 3
WEEKS = 53
DAYS_IN_WEEK = 7

# Animation parameters
ANIMATION_DURATION = 0.8 # Total time for the diagonal reveal
STAGGER = 0.015          # Delay between boxes appearing

def render_heatmap():
    if not os.path.exists(INPUT_JSON):
        print(f"Error: {INPUT_JSON} not found. Run fetch_contributions.py first.")
        return

    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    days = data.get("days", [])
    if not days:
        print("No contribution days found in JSON.")
        return

    # Calculate grid dimensions
    svg_width = WEEKS * (BOX_SIZE + BOX_SPACING) + 40
    svg_height = DAYS_IN_WEEK * (BOX_SIZE + BOX_SPACING) + 40

    # We expect up to 371 days (53 weeks * 7 days)
    # The data from GitHub is chronological. We fill columns (weeks) top-to-bottom.
    
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">
    <style>
        .box {{
            opacity: 0;
            animation: fadeIn 0.4s ease-out forwards;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: scale(0.5); }}
            to {{ opacity: 1; transform: scale(1); }}
        }}
        .text {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            font-size: 10px;
            fill: #8b949e;
        }}
    </style>
    
    <!-- Background (optional) -->
    <!-- <rect width="100%" height="100%" fill="#0d1117" /> -->
    
    <g transform="translate(20, 20)">
    """

    # Add day labels (Mon, Wed, Fri)
    svg_content += f'<text class="text" x="-15" y="{2 * (BOX_SIZE + BOX_SPACING) - 3}">Mon</text>\n'
    svg_content += f'<text class="text" x="-15" y="{4 * (BOX_SIZE + BOX_SPACING) - 3}">Wed</text>\n'
    svg_content += f'<text class="text" x="-15" y="{6 * (BOX_SIZE + BOX_SPACING) - 3}">Fri</text>\n'

    # Map the days into a grid
    for i, day in enumerate(days):
        week_idx = i // 7
        day_idx = i % 7
        
        import random
        if week_idx < (WEEKS // 2):
            # Fill the left half, but randomly leave a few empty (around 3-4 total)
            if random.random() < 0.02:
                level = 0
            else:
                level = random.randint(1, len(PALETTE) - 1)
        else:
            # Empty out the right half
            level = 0
            
        color = PALETTE[level]
        
        x = week_idx * (BOX_SIZE + BOX_SPACING)
        y = day_idx * (BOX_SIZE + BOX_SPACING)
        
        # Sine wave animation reveal
        wave_offset = math.sin(week_idx * 0.2 + day_idx * 0.5) * 10
        delay = (week_idx * 2 + day_idx + wave_offset) * STAGGER
        
        svg_content += f'      <rect class="box" x="{x}" y="{y}" width="{BOX_SIZE}" height="{BOX_SIZE}" rx="2" fill="{color}" style="animation-delay: {delay}s; transform-origin: {x + BOX_SIZE/2}px {y + BOX_SIZE/2}px;" />\n'

    svg_content += """    </g>
</svg>"""

    with open(OUTPUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    print(f"Created {OUTPUT_SVG}")

if __name__ == "__main__":
    render_heatmap()
