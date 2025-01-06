from db import db

from models.game_elements import GameElements
from models.app_users import AppUsers
from models.collections import Collections
from models.types import Types
from models.notes import Notes

def add_game_elements(collection_name, type_name, elements_list):
    collection_query = db.session.query(Collections).filter(Collections.name == collection_name).first()
    type_query = db.session.query(Types).filter(Types.name == type_name).first()
    user_query = db.session.query(AppUsers).filter(AppUsers.email == "super@test.com").first()

    for game_element in elements_list:
        if not db.session.query(GameElements).filter(GameElements.name == game_element["name"]).first():
            name = game_element["name"]
            description = game_element["description"]
            image_url = game_element["image_url"]
            new_game_element = GameElements(name, description, None, None, image_url)
            new_game_element.collection_id = collection_query.collection_id
            new_game_element.type_id = type_query.type_id

            db.session.add(new_game_element)
            db.session.flush()

            if "notes" in game_element and game_element["notes"]:
                for note in game_element["notes"]:
                    new_note = Notes(user_query.user_id, None, note, "", "", None)
                    new_note.element_id = new_game_element.element_id
                    db.session.add(new_note)
            
    db.session.commit()