from flask import jsonify

from db import db
from models.items import Items, item_schema, items_schema
from models.collections import Collections
from models.types import Types
from models.tags import Tags
from util.controllers_util import *
from lib.authenticate import auth, validate_uuid4


@auth
def item_add(req):
    post_data = req.form if req.form else req.json
    if not validate_uuid4(post_data.get("collection_id") or not validate_uuid4(post_data.get("type_id"))):
        return jsonify({"message": "could not create item, must provide valid uuids for collection id and type id"}), 400
    
    collection_query = db.session.query(Collections).filter(Collections.collection_id == post_data.get("collection_id")).first()
    if  not collection_query:
        return jsonify({"message": "could not create item, collection does not exist"})
    
    type_query = db.session.query(Types).filter(Types.type_id == post_data.get("type_id")).first()
    if  not type_query:
        return jsonify({"message": "could not create item, type does not exist"})

    return record_add(req, Items.new_item_obj(), item_schema, "item")
    

@auth
def item_tag_update(req):
    post_data = req.form if req.form else req.json

    item_id = post_data.get('item_id')
    tag_id = post_data.get('tag_id')

    item_query = db.session.query(Items).filter(Items.item_id == item_id).first()
    tag_query = db.session.query(Tags).filter(Tags.tag_id == tag_id).first()

    if not validate_uuid4(item_id) or not validate_uuid4(tag_id):
        return jsonify({"message": "cannot add tag to item without valid uuids"})

    if item_query:
        if tag_query:
            tag_ids = []
            for tag in item_query.tags:
                tag_ids.append(str(tag.tag_id))

            if tag_id in tag_ids:
                item_query.tags.remove(tag_query)
            else:
                item_query.tags.append(tag_query)

            db.session.commit()
        else:
            return jsonify({"message": "cannot add tag to item, tag does not exist"})
    else:
        return jsonify({"message": "cannot add tag, item does not exist"})

    return jsonify({"message": "tag added to game item", "result": item_schema.dump(item_query)}), 200    
    

# @auth
def items_get_all():
    return records_get_all(Items, items_schema, "items")


# @auth
def items_get_all_with_tag(tag_id):
    items_query = db.session.query(Items).filter(Tags.tag_id == tag_id).all()

    if not items_query:
        return jsonify({"message": f"no items found with that tag"}), 404
    
    return jsonify({"message": f"items found", "results": items_schema.dump(items_query)}), 200


# @auth
def item_get_by_id(item_id):
    if not validate_uuid4(item_id):
        return jsonify({"message": "cannot get item without a valid uuid"})

    item_query = db.session.query(Items).filter(Items.item_id == item_id).first()
    return record_get_by_id(item_query, item_schema, "item")


@auth
def item_update_by_id(req, item_id):
    if not validate_uuid4(item_id):
        return jsonify({"message": "cannot update item without a valid uuid"})

    item_query = db.session.query(Items).filter(Items.item_id == item_id).first()
    return record_update_by_id(req, item_query, item_schema, "item")


@auth
def item_delete_by_id(item_id):
    if not validate_uuid4(item_id):
        return jsonify({"message": "cannot update item without a valid uuid"})

    item_query = db.session.query(Items).filter(Items.item_id == item_id).first()
    return record_delete_by_id(item_query, "item")
        