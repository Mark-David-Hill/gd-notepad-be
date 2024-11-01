from db import db

from models.game_elements import GameElements
from models.tags import Tags

def add_tags(elements_list):
    for game_element in elements_list:
        if "tags" in game_element and game_element["tags"]:
            for tag in game_element["tags"]:
                element_1_id_query = db.session.query(GameElements).filter(GameElements.name == game_element["name"]).first().element_id
                new_tag = Tags("", tag.name, tag.description)
                db.session.add(new_tag)

        db.session.commit()


def __init__(self, type_id, tag_name, description):
        self.type_id = type_id
        self.tag_name = tag_name
        self.description = description

def new_tag_obj():
    return Tags("", "", "")