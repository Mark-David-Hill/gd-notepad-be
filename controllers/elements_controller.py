from flask import jsonify
from uuid import UUID

from db import db
from models.game_elements import GameElements, game_element_schema, game_elements_schema
from models.tags import Tags
from util.reflection import populate_object
from util.controllers_util import record_add, records_get_all
from lib.authenticate import auth, validate_uuid4


@auth
def element_add(req):
    return record_add(req, GameElements.new_element_obj(), game_element_schema, "element")
    

@auth
def element_tag_update(req):
    post_data = req.form if req.form else req.json

    element_id = post_data.get('element_id')
    tag_id = post_data.get('tag_id')

    element_query = db.session.query(GameElements).filter(GameElements.element_id == element_id).first()
    tag_query = db.session.query(Tags).filter(Tags.tag_id == tag_id).first()

    if element_query:
        if tag_query:
            tag_ids = []
            for tag in element_query.tags:
                tag_ids.append(str(tag.tag_id))

            if tag_id in tag_ids:
                element_query.tags.remove(tag_query)
            else:
                element_query.tags.append(tag_query)

            db.session.commit()

    element_query = db.session.query(GameElements).filter(GameElements.element_id == element_id).first()

    return jsonify({"message": "tag added to game element", "result": game_element_schema.dump(element_query)}), 200    
    

@auth
def elements_get_all():
    return records_get_all(GameElements, game_elements_schema, "elements")


@auth
def element_get_by_id(element_id):
    if not validate_uuid4(element_id):
        return jsonify({"message": "cannot get element without a valid uuid"})

    element_query = db.session.query(GameElements).filter(GameElements.element_id == element_id).first()

    if not element_query:
        return jsonify({"message": "element does not exist"}), 404
    
    return jsonify({"message": "element found", "result": game_element_schema.dump(element_query)}), 200


@auth
def element_update_by_id(req, element_id):
    post_data = req.form if req.form else req.json

    if not validate_uuid4(element_id):
        return jsonify({"message": "cannot update element without a valid uuid"})

    element_query = db.session.query(GameElements).filter(GameElements.element_id == element_id).first()

    populate_object(element_query, post_data)

    if not element_query:
        return jsonify({"message": "element does not exist"}), 404
    
    
    db.session.commit()
    return jsonify({"message": "element updated", "result": game_element_schema.dump(element_query)}), 201


@auth
def element_delete_by_id(element_id):
    if not validate_uuid4(element_id):
        return jsonify({"message": "cannot update element without a valid uuid"})

    element_query = db.session.query(GameElements).filter(GameElements.element_id == element_id).first()

    if not element_query:
        return jsonify({"message": "element does not exist"}), 404
    
    try:
        db.session.delete(element_query)
        db.session.commit()
        return jsonify({"message": "the element was deleted"}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not delete element"})
        