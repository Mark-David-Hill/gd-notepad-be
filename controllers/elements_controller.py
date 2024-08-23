from flask import jsonify

from db import db
from models.game_elements import GameElements, game_element_schema, game_elements_schema
from models.games import Games
from models.types import Types
from models.tags import Tags
from util.controllers_util import *
from lib.authenticate import auth, validate_uuid4


@auth
def element_add(req):
    post_data = req.form if req.form else req.json
    if not validate_uuid4(post_data.get("game_id") or not validate_uuid4(post_data.get("type_id"))):
        return jsonify({"message": "could not create element, must provide valid uuids for game id and type id"}), 400
    
    game_query = db.session.query(Games).filter(Games.game_id == post_data.get("game_id")).first()
    if  not game_query:
        return jsonify({"message": "could not create element, game does not exist"})
    
    type_query = db.session.query(Types).filter(Types.type_id == post_data.get("type_id")).first()
    if  not type_query:
        return jsonify({"message": "could not create element, type does not exist"})

    return record_add(req, GameElements.new_element_obj(), game_element_schema, "element")
    

@auth
def element_tag_update(req):
    post_data = req.form if req.form else req.json

    element_id = post_data.get('element_id')
    tag_id = post_data.get('tag_id')

    element_query = db.session.query(GameElements).filter(GameElements.element_id == element_id).first()
    tag_query = db.session.query(Tags).filter(Tags.tag_id == tag_id).first()

    if not validate_uuid4(element_id) or not validate_uuid4(tag_id):
        return jsonify({"message": "cannot add tag to element without valid uuids"})

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
        else:
            return jsonify({"message": "cannot add tag to element, tag does not exist"})
    else:
        return jsonify({"message": "cannot add tag, element does not exist"})

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
    return record_get_by_id(element_query, game_element_schema, "element")


@auth
def element_update_by_id(req, element_id):
    if not validate_uuid4(element_id):
        return jsonify({"message": "cannot update element without a valid uuid"})

    element_query = db.session.query(GameElements).filter(GameElements.element_id == element_id).first()
    return record_update_by_id(req, element_query, game_element_schema, "element")


@auth
def element_delete_by_id(element_id):
    if not validate_uuid4(element_id):
        return jsonify({"message": "cannot update element without a valid uuid"})

    element_query = db.session.query(GameElements).filter(GameElements.element_id == element_id).first()
    return record_delete_by_id(element_query, "element")
        