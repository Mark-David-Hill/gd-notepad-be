from db import db

from models.color_schemes import ColorSchemes

color_scheme_list = [
    {
        "name": "Bright Gold",
        "primary_color": "#FFD700",  # Gold
        "secondary_color": "#FFA500",  # Orange
        "text_color": "#2F4F4F",  # Dark Slate Gray
        "background_color": "#FFFACD",  # Lemon Chiffon
    },
    {
        "name": "Deep Blue",
        "primary_color": "#0077B6",  # Deep Cyan
        "secondary_color": "#0096C7",  # Sky Blue
        "text_color": "#FFFFFF",  # White
        "background_color": "#CAF0F8",  # Light Aqua
    },
    {
        "name": "Night Mode",
        "primary_color": "#2C2C54",  # Deep Indigo
        "secondary_color": "#706FD3",  # Soft Purple
        "text_color": "#D1D1D1",  # Light Gray
        "background_color": "#1E1E3F",  # Dark Navy
    },
    {
        "name": "Woodland",
        "primary_color": "#4CAF50",  # Forest Green
        "secondary_color": "#8BC34A",  # Light Green
        "text_color": "#1B1B1B",  # Almost Black
        "background_color": "#E8F5E9",  # Pale Green
    },
    {
        "name": "Frosted Ice",
        "primary_color": "#85C1E9",  # Light Blue
        "secondary_color": "#D6EAF8",  # Very Pale Blue
        "text_color": "#2E4053",  # Steel Gray
        "background_color": "#EBF5FB",  # Ice White
    },
    {
        "name": "Neutral Gray",
        "primary_color": "#3D3D3D",  # Charcoal Gray
        "secondary_color": "#AAAAAA",  # Light Gray
        "text_color": "#FFFFFF",  # White
        "background_color": "#F2F2F2",  # Soft Gray
    },
    {
        "name": "Fiery Red",
        "primary_color": "#D72638",  # Crimson
        "secondary_color": "#FF5C5C",  # Light Red
        "text_color": "#1A1A1A",  # Almost Black
        "background_color": "#FFE6E6",  # Light Pink
    },
    {
        "name": "Amber Glow",
        "primary_color": "#F39C12",  # Amber
        "secondary_color": "#F7DC6F",  # Light Yellow
        "text_color": "#1B1B1B",  # Almost Black
        "background_color": "#FFF8E1",  # Pale Yellow
    },
    {
        "name": "Berry Pop",
        "primary_color": "#C2185B",  # Raspberry
        "secondary_color": "#E91E63",  # Hot Pink
        "text_color": "#FFFFFF",  # White
        "background_color": "#F8BBD0",  # Light Pink
    },
    {
        "name": "Rustic Earth",
        "primary_color": "#8B4513",  # Saddle Brown
        "secondary_color": "#D2691E",  # Chocolate
        "text_color": "#FDF5E6",  # Old Lace
        "background_color": "#FAF3E0",  # Off White
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