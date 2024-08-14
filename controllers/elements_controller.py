from flask import jsonify
from uuid import UUID

from db import db
from models.game_elements import GameElements, game_element_schema, game_elements_schema
from util.reflection import populate_object
from lib.authenticate import auth


@auth
def element_add(req):
    post_data = req.form if req.form else req.json

    if not post_data:
        return jsonify({"message": "all required fields must be submitted"})
    
    new_element = GameElements.new_element_obj()

    populate_object(new_element, post_data)

    try:
        db.session.add(new_element)
        db.session.commit()
        return jsonify({"message": "element created", "result": game_element_schema.dump(new_element)}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not create element"})
    
    

@auth
def elements_get_all():
    elements_query = db.session.query(GameElements).all()

    if not elements_query:
        return jsonify({"message": "no elements found"}), 404
    
    return jsonify({"message": "elements found", "results": game_elements_schema.dump(elements_query)}), 200


@auth
def element_get_by_id(element_id):
    try:
        UUID(element_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot get element without a valid uuid"})

    element_query = db.session.query(GameElements).filter(GameElements.element_id == element_id).first()

    if not element_query:
        return jsonify({"message": "element does not exist"}), 404
    
    return jsonify({"message": "element found", "result": game_element_schema.dump(element_query)}), 200


@auth
def element_update_by_id(req, element_id):
    post_data = req.form if req.form else req.json

    try:
        UUID(element_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot update element without a valid uuid"})

    element_query = db.session.query(GameElements).filter(GameElements.element_id == element_id).first()

    populate_object(element_query, post_data)

    if not element_query:
        return jsonify({"message": "element does not exist"}), 404
    
    try:
        db.session.commit()
        return jsonify({"message": "element updated", "result": game_element_schema.dump(element_query)}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not update element"})


@auth
def element_delete_by_id(element_id):
    try:
        UUID(element_id, version=4)
    except Exception as e:
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
        