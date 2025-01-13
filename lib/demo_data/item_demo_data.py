from db import db

from models.collections import Collections
from models.app_users import AppUsers
from models.items import Items
from models.types import Types
from models.notes import Notes

def add_items(collection_name, type_name, items_list):
    collection_query = db.session.query(Collections).filter(Collections.name == collection_name).first()
    type_query = db.session.query(Types).filter(Types.name == type_name).first()
    user_query = db.session.query(AppUsers).filter(AppUsers.email == "super@test.com").first()

    for item in items_list:
        if not db.session.query(Items).filter(Items.name == item["name"]).first():
            name = item["name"]
            description = item["description"]
            image_url = item["image_url"]
            new_item = Items(name, description, None, None, image_url)
            new_item.collection_id = collection_query.collection_id
            new_item.type_id = type_query.type_id
            new_item.user_created_by_id = user_query.user_id

            db.session.add(new_item)
            db.session.flush()

            if "notes" in item and item["notes"]:
                for note in item["notes"]:
                    new_note = Notes(user_query.user_id, None, note, "", "", None)
                    new_note.item_id = new_item.item_id
                    db.session.add(new_note)
            
    db.session.commit()