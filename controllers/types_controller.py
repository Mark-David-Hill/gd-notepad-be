from flask import jsonify
from uuid import UUID

from db import db
from models.types import Types, type_schema, types_schema
from util.reflection import populate_object
from lib.authenticate import auth


@auth
def type_add(req):
    post_data = req.form if req.form else req.json

    if not post_data:
        return jsonify({"message": "all required fields must be submitted"})
    
    new_type = Types.new_type_obj()

    populate_object(new_type, post_data)

    try:
        db.session.add(new_type)
        db.session.commit()
        return jsonify({"message": "type created", "result": type_schema.dump(new_type)}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not create type"})
    
    
@auth
def types_get_all():
    types_query = db.session.query(Types).all()

    if not types_query:
        return jsonify({"message": "no types found"}), 404
    
    return jsonify({"message": "types found", "results": types_schema.dump(types_query)}), 200


@auth
def type_get_by_id(type_id):
    try:
        UUID(type_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot get type without a valid uuid"})

    type_query = db.session.query(Types).filter(Types.type_id == type_id).first()

    if not type_query:
        return jsonify({"message": "type does not exist"}), 404
    
    return jsonify({"message": "type found", "result": type_schema.dump(type_query)}), 200


@auth
def type_update_by_id(req, type_id):
    post_data = req.form if req.form else req.json

    try:
        UUID(type_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot update type without a valid uuid"})

    type_query = db.session.query(Types).filter(Types.type_id == type_id).first()

    populate_object(type_query, post_data)

    if not type_query:
        return jsonify({"message": "type does not exist"}), 404
    
    try:
        db.session.commit()
        return jsonify({"message": "type updated", "result": type_schema.dump(type_query)}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not update type"})


@auth
def type_delete_by_id(type_id):
    try:
        UUID(type_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot update type without a valid uuid"})

    type_query = db.session.query(Types).filter(Types.type_id == type_id).first()

    if not type_query:
        return jsonify({"message": "type does not exist"}), 404
    
    try:
        db.session.delete(type_query)
        db.session.commit()
        return jsonify({"message": "the type was deleted"}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not delete type"})
        