from flask import jsonify

from db import db
from models.color_schemes import ColorSchemes, color_scheme_schema, color_schemes_schema
from util.controllers_util import *
from lib.authenticate import auth, validate_uuid4


@auth
def color_scheme_add(req):
    return record_add(req, ColorSchemes.new_color_scheme_obj(), color_scheme_schema, "color_scheme")
    
    
# @auth
def color_schemes_get_all():
    return records_get_all(ColorSchemes, color_schemes_schema, "color_schemes")


# def types_get_by_collection(collection_id):
#     return records_get_by_collection(Types, types_schema, "types", collection_id)


# # @auth
# def type_get_by_id(type_id):
#     if not validate_uuid4(type_id):
#         return jsonify({"message": "cannot get type without a valid uuid"}), 400

#     type_query = db.session.query(Types).filter(Types.type_id == type_id).first()
#     return record_get_by_id(type_query, type_schema, "type")


# @auth
# def type_update_by_id(req, type_id):
#     if not validate_uuid4(type_id):
#         return jsonify({"message": "cannot update type without a valid uuid"}), 400

#     type_query = db.session.query(Types).filter(Types.type_id == type_id).first()
#     return record_update_by_id(req, type_query, type_schema, "type")


# @auth
# def type_delete_by_id(type_id):
#     if not validate_uuid4(type_id):
#         return jsonify({"message": "cannot update type without a valid uuid"}), 400

#     type_query = db.session.query(Types).filter(Types.type_id == type_id).first()
#     return record_delete_by_id(type_query, "type")