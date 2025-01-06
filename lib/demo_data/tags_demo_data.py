from db import db

from models.items import Items
from models.tags import Tags

def add_tags(items_list):
    for item in items_list:
        if "tags" in item and item["tags"]:
            for tag in item["tags"]:
                # item_1_id_query = db.session.query(Items).filter(Items.name == item["name"]).first().item_id
                new_tag = Tags("", tag.name, tag.description)
                db.session.add(new_tag)

        db.session.commit()


def __init__(self, type_id, tag_name, description):
        self.type_id = type_id
        self.tag_name = tag_name
        self.description = description

def new_tag_obj():
    return Tags("", "", "")