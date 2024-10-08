from db import db

from models.game_elements import GameElements
from models.games import Games
from models.types import Types

def add_game_elements(game_name, type_name, elements_list):
    game_query = db.session.query(Games).filter(Games.name == game_name).first()
    type_query = db.session.query(Types).filter(Types.name == type_name).first()
    for index, game_element in enumerate(elements_list):
        if not db.session.query(GameElements).filter(GameElements.name == game_element["name"]).first():
            name = game_element["name"]
            description = game_element["description"]
            image_url = game_element["image_url"]
            new_game_element = GameElements(name, description, None, None, image_url)
            new_game_element.game_id = game_query.game_id
            new_game_element.type_id = type_query.type_id

            db.session.add(new_game_element)
            
    db.session.commit()
