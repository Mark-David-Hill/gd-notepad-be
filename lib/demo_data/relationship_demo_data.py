from db import db

from models.relationships import Relationships
from models.items import Items

def add_relationships(items_list):
    for item in items_list:
        if "relationships" in item and item["relationships"]:
            for relationship in item["relationships"]:
                count = relationship["count"] if "count" in relationship else 0
                item_1_id_query = db.session.query(Items).filter(Items.name == item["name"]).first().item_id
                item_2_id_query = db.session.query(Items).filter(Items.name == relationship["name"]).first().item_id
                new_relationship = Relationships(item_1_id_query, item_2_id_query, relationship["description"], count)
                db.session.add(new_relationship)
    
        db.session.commit()
