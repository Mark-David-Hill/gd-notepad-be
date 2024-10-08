from db import db

from models.game_elements import GameElements
from models.games import Games
from models.types import Types


levels_list = [
    {
        "description": "The first level, a grassy overworld with Goombas and Koopas.",
        "image_url": "",
        "name": "1-1"
    },
    {
        "description": "An underground level featuring pipes and Piranha Plants.",
        "image_url": "",
        "name": "1-2"
    },
    {
        "description": "An above-ground level with platforms and bridges.",
        "image_url": "",
        "name": "1-3"
    },
    {
        "description": "The first castle level, with firebars and Bowser at the end.",
        "image_url": "",
        "name": "1-4"
    },
    {
        "description": "Another overworld level, similar to 1-1 but slightly harder.",
        "image_url": "",
        "name": "2-1"
    },
    {
        "description": "An underground level with more pipes and tricky platforming.",
        "image_url": "",
        "name": "2-2"
    },
    {
        "description": "A sky level with platforms and moving lifts.",
        "image_url": "",
        "name": "2-3"
    },
    {
        "description": "A castle level with a more difficult layout and Bowser.",
        "image_url": "",
        "name": "2-4"
    },
    {
        "description": "An overworld level introducing more enemies and tougher platforming.",
        "image_url": "",
        "name": "3-1"
    },
    {
        "description": "An underwater level with Bloopers and Cheep Cheeps.",
        "image_url": "",
        "name": "3-2"
    },
    {
        "description": "Another sky level with more challenging platforming.",
        "image_url": "",
        "name": "3-3"
    },
    {
        "description": "A castle level with firebars, lava, and Bowser.",
        "image_url": "",
        "name": "3-4"
    },
    {
        "description": "A difficult overworld level with Lakitus and Spinies.",
        "image_url": "",
        "name": "4-1"
    },
    {
        "description": "A second underground level with many Piranha Plants.",
        "image_url": "",
        "name": "4-2"
    },
    {
        "description": "A platform-heavy sky level with moving platforms.",
        "image_url": "",
        "name": "4-3"
    },
    {
        "description": "A tricky castle level with more firebars and Bowser.",
        "image_url": "",
        "name": "4-4"
    },
    {
        "description": "An overworld level with Hammer Bros and tricky jumps.",
        "image_url": "",
        "name": "5-1"
    },
    {
        "description": "An underground level featuring Bullet Bills.",
        "image_url": "",
        "name": "5-2"
    },
    {
        "description": "A bridge level with many Cheep Cheeps.",
        "image_url": "",
        "name": "5-3"
    },
    {
        "description": "A castle level with more complex firebar patterns and Bowser.",
        "image_url": "",
        "name": "5-4"
    },
    {
        "description": "An overworld level with harder platforming and enemies.",
        "image_url": "",
        "name": "6-1"
    },
    {
        "description": "Another underground level with tricky platforming.",
        "image_url": "",
        "name": "6-2"
    },
    {
        "description": "A sky level with more moving platforms and lifts.",
        "image_url": "",
        "name": "6-3"
    },
    {
        "description": "A castle level with a maze-like structure and Bowser.",
        "image_url": "",
        "name": "6-4"
    },
    {
        "description": "An overworld level with more enemies and obstacles.",
        "image_url": "",
        "name": "7-1"
    },
    {
        "description": "An underground level with more pipes and enemies.",
        "image_url": "",
        "name": "7-2"
    },
    {
        "description": "A sky level with many moving platforms.",
        "image_url": "",
        "name": "7-3"
    },
    {
        "description": "A castle level with more firebars and Bowser.",
        "image_url": "",
        "name": "7-4"
    },
    {
        "description": "An overworld level with Hammer Bros and tricky platforming.",
        "image_url": "",
        "name": "8-1"
    },
    {
        "description": "A very challenging underground level with many enemies.",
        "image_url": "",
        "name": "8-2"
    },
    {
        "description": "A sky level with precise platforming and enemies.",
        "image_url": "",
        "name": "8-3"
    },
    {
        "description": "The final castle level, with a maze and Bowser as the final boss.",
        "image_url": "",
        "name": "8-4"
    }
]


def add_levels():
    game_query = db.session.query(Games).filter(Games.name == "Super Mario Bros.").first()
    type_query = db.session.query(Types).filter(Types.name == "Level").first()
    for index, game_element in enumerate(levels_list):
        if not db.session.query(GameElements).filter(GameElements.name == game_element["name"]).first():

            name = game_element["name"]
            description = game_element["description"]
            image_url = game_element["image_url"]
            new_game_element = GameElements(name, description, None, None, image_url)
            new_game_element.game_id = game_query.game_id
            new_game_element.type_id = type_query.type_id

            db.session.add(new_game_element)
            
    db.session.commit()

