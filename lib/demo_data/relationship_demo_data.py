from db import db

from models.element_relationships import ElementRelationships
from models.game_elements import GameElements

def add_relationships(elements_list):
    for game_element in elements_list:
        
        if "relationships" in game_element and game_element["relationships"]:
            for relationship in game_element["relationships"]:
                count = relationship["count"] if "count" in relationship else 0
                element_1_id_query = db.session.query(GameElements).filter(GameElements.name == game_element["name"]).first().element_id
                element_2_id_query = db.session.query(GameElements).filter(GameElements.name == relationship["name"]).first().element_id
                new_relationship = ElementRelationships(element_1_id_query, element_2_id_query, relationship["description"], count)
                db.session.add(new_relationship)

        db.session.commit()
