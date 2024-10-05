from db import db

from models.game_elements import GameElements
from models.games import Games
from models.types import Types


enemies_list = [
    {
        "description": "A Mario enemy",
        "image_url": "",
        "name": "Goomba"
    },
    {
        "description": "A turtle-like enemy that can be kicked",
        "image_url": "",
        "name": "Koopa Troopa"
    },
    {
        "description": "A faster, winged version of Koopa Troopa",
        "image_url": "",
        "name": "Koopa Paratroopa"
    },
    {
        "description": "A spiked enemy that cannot be jumped on",
        "image_url": "",
        "name": "Spiny"
    },
    {
        "description": "A flying, beetle-like enemy",
        "image_url": "",
        "name": "Buzzy Beetle"
    },
    {
        "description": "A squid-like underwater enemy",
        "image_url": "",
        "name": "Blooper"
    },
    {
        "description": "A fish that swims in underwater levels",
        "image_url": "",
        "name": "Cheep Cheep"
    },
    {
        "description": "A fire-breathing enemy, often found in castles",
        "image_url": "",
        "name": "Firebar"
    },
    {
        "description": "A hammer-throwing enemy",
        "image_url": "",
        "name": "Hammer Bro"
    },
    {
        "description": "A green dragon-like enemy that shoots fireballs",
        "image_url": "",
        "name": "Bowser"
    },
    {
        "description": "A plant that emerges from pipes",
        "image_url": "",
        "name": "Piranha Plant"
    },
    {
        "description": "A cannonball-like projectile shot from Bill Blasters",
        "image_url": "",
        "name": "Bullet Bill"
    },
    {
        "description": "A spiked shell enemy thrown by Lakitu",
        "image_url": "",
        "name": "Spiny Egg"
    },
    {
        "description": "A cloud-riding enemy that throws Spinies",
        "image_url": "",
        "name": "Lakitu"
    }
]


def add_enemies():
    game_query = db.session.query(Games).filter(Games.name == "Super Mario Bros.").first()
    type_query = db.session.query(Types).filter(Types.name == "Enemy Element").first()
    for index, game_element in enumerate(enemies_list):
        if not db.session.query(GameElements).filter(GameElements.name == game_element["name"]).first():

            name = game_element["name"]
            description = game_element["description"]
            image_url = game_element["image_url"]
            new_game_element = GameElements(name, description, None, None, image_url)
            new_game_element.game_id = game_query.game_id
            new_game_element.type_id = type_query.type_id

            db.session.add(new_game_element)
            
    db.session.commit()

