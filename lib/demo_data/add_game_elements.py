from db import db

from models.element_relationships import ElementRelationships
from models.game_elements import GameElements
from models.app_users import AppUsers
from models.games import Games
from models.types import Types
from models.notes import Notes

def add_game_elements(game_name, type_name, elements_list):
    game_query = db.session.query(Games).filter(Games.name == game_name).first()
    type_query = db.session.query(Types).filter(Types.name == type_name).first()
    user_query = db.session.query(AppUsers).filter(AppUsers.email == "super@test.com").first()
    for index, game_element in enumerate(elements_list):
        if not db.session.query(GameElements).filter(GameElements.name == game_element["name"]).first():
            name = game_element["name"]
            description = game_element["description"]
            image_url = game_element["image_url"]
            new_game_element = GameElements(name, description, None, None, image_url)
            new_game_element.game_id = game_query.game_id
            new_game_element.type_id = type_query.type_id

            db.session.add(new_game_element)
            db.session.flush()

            if "notes" in game_element and game_element["notes"]:
                for note in game_element["notes"]:
                    new_note = Notes(user_query.user_id, None, note, "", "", None)
                    new_note.element_id = new_game_element.element_id
                    db.session.add(new_note)
            
            
    db.session.commit()

    for index, game_element in enumerate(elements_list):
        
        if "relationships" in game_element and game_element["relationships"]:
            for relationship in game_element["relationships"]:
                count = relationship["count"] if "count" in relationship else 0
                element_1_id_query = db.session.query(GameElements).filter(GameElements.name == game_element["name"]).first().element_id
                element_2_id_query = db.session.query(GameElements).filter(GameElements.name == relationship["name"]).first().element_id
                new_relationship = ElementRelationships(element_1_id_query, element_2_id_query, relationship["description"], count)
                db.session.add(new_relationship)

        db.session.commit()
