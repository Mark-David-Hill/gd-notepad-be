from db import db

from models.color_schemes import ColorSchemes

color_scheme_list = [
    {
        "name": "Sunny Vibes",
        "primary_color": "#FFEE58",  # Yellow
        "secondary_color": "#FFD740",  # Amber
        "text_color": "#000000",  # Black
        "background_color": "#FFF9C4",  # Light yellow
    },
    {
        "name": "Ocean Breeze",
        "primary_color": "#0288D1",  # Light blue
        "secondary_color": "#03A9F4",  # Sky blue
        "text_color": "#FFFFFF",  # White
        "background_color": "#E1F5FE",  # Very light blue
    },
    {
        "name": "Forest Glow",
        "primary_color": "#388E3C",  # Forest green
        "secondary_color": "#4CAF50",  # Leaf green
        "text_color": "#FFFFFF",  # White
        "background_color": "#E8F5E9",  # Very light green
    },
    {
        "name": "Desert Sunset",
        "primary_color": "#FF5722",  # Bright orange
        "secondary_color": "#FF7043",  # Lighter orange
        "text_color": "#FFFFFF",  # White
        "background_color": "#FFE0B2",  # Light peach
    },
    {
        "name": "Lavender Dream",
        "primary_color": "#7E57C2",  # Lavender purple
        "secondary_color": "#9575CD",  # Light lavender
        "text_color": "#FFFFFF",  # White
        "background_color": "#EDE7F6",  # Very light lavender
    },
    {
        "name": "Midnight Bliss",
        "primary_color": "#263238",  # Deep blue-gray
        "secondary_color": "#37474F",  # Dark gray
        "text_color": "#FFFFFF",  # White
        "background_color": "#CFD8DC",  # Light gray
    },
    {
        "name": "Candy Pop",
        "primary_color": "#E91E63",  # Hot pink
        "secondary_color": "#F06292",  # Light pink
        "text_color": "#FFFFFF",  # White
        "background_color": "#FCE4EC",  # Very light pink
    },
    {
        "name": "Autumn Hues",
        "primary_color": "#795548",  # Brown
        "secondary_color": "#A1887F",  # Light brown
        "text_color": "#FFFFFF",  # White
        "background_color": "#D7CCC8",  # Beige
    },
    {
        "name": "Ice Frost",
        "primary_color": "#00BCD4",  # Cyan
        "secondary_color": "#B2EBF2",  # Light cyan
        "text_color": "#000000",  # Black
        "background_color": "#E0F7FA",  # Very light cyan
    },
    {
        "name": "Crimson Passion",
        "primary_color": "#D32F2F",  # Deep red
        "secondary_color": "#E57373",  # Lighter red
        "text_color": "#FFFFFF",  # White
        "background_color": "#FFEBEE",  # Light pink-red
    },
]


def add_color_schemes():

    for index, color_scheme in enumerate(color_scheme_list):
        if not db.session.query(ColorSchemes).filter(ColorSchemes.name == color_scheme["name"]).first():
            name = color_scheme["name"]
            primary_color = color_scheme["primary_color"]
            secondary_color = color_scheme["secondary_color"]
            text_color = color_scheme["text_color"]
            background_color = color_scheme["background_color"]
            new_color_scheme = ColorSchemes(name, primary_color, secondary_color, text_color, background_color)


            db.session.add(new_color_scheme)
            
    db.session.commit()