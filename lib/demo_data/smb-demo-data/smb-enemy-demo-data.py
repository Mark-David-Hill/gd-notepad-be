from db import db

from models.game_elements import GameElements
from lib.demo_data.smb_demo_data.smb_seed_data import enemy_elements

def add_smb_enemies():
    for index, enemy in enumerate(enemy_elements):
        if not db.session.query(Games).filter(Games.name == game["name"]).first():

            # name = game["name"]
            # description = game["description"]
            # series = game["series"]
            # genre = game["genre"]
            # new_game = Games(name, description, series, genre)

            # db.session.add(new_game)
            # db.session.commit()


# {
#     "type_id": "{{recentTypeId}}",
#     "game_id": "{{recentGameId}}",
#     "name": "Goomba",
#     "description": "A Mario enemy",
#     "image_url": "goomba.png"
# }