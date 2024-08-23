from flask import jsonify

from db import db
from models.types import Types, type_schema, types_schema
from util.reflection import populate_object
from util.controllers_util import *
from lib.authenticate import auth, validate_uuid4


@auth
def type_add(req):
    return record_add(req, Types.new_type_obj(), type_schema, "type")
    
    
@auth
def types_get_all():
    return records_get_all(Types, types_schema, "types")


@auth
def type_get_by_id(type_id):
    if not validate_uuid4(type_id):
        return jsonify({"message": "cannot get type without a valid uuid"}), 400

    type_query = db.session.query(Types).filter(Types.type_id == type_id).first()
    return record_get_by_id(type_query, type_schema, "type")


@auth
def type_update_by_id(req, type_id):
    if not validate_uuid4(type_id):
        return jsonify({"message": "cannot update type without a valid uuid"}), 400

    type_query = db.session.query(Types).filter(Types.type_id == type_id).first()
    return record_update_by_id(req, type_query, type_schema, "type")


@auth
def type_delete_by_id(type_id):
    if not validate_uuid4(type_id):
        return jsonify({"message": "cannot update type without a valid uuid"}), 400

    type_query = db.session.query(Types).filter(Types.type_id == type_id).first()
    return record_delete_by_id(type_query, "type")