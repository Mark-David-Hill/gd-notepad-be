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


# @auth
def color_scheme_get_by_id(color_scheme_id):
    if not validate_uuid4(color_scheme_id):
        return jsonify({"message": "cannot get color scheme without a valid uuid"}), 400

    color_scheme_query = db.session.query(ColorSchemes).filter(ColorSchemes.color_scheme_id == color_scheme_id).first()
    return record_get_by_id(color_scheme_query, color_scheme_schema, "color_scheme")


# @auth
def color_scheme_update_by_id(req, color_scheme_id):
    if not validate_uuid4(color_scheme_id):
        return jsonify({"message": "cannot update color scheme without a valid uuid"}), 400

    color_scheme_query = db.session.query(ColorSchemes).filter(ColorSchemes.color_scheme_id == color_scheme_id).first()
    return record_update_by_id(req, color_scheme_query, color_scheme_schema, "color_scheme")


# @auth
def color_scheme_delete_by_id(color_scheme_id):
    if not validate_uuid4(color_scheme_id):
        return jsonify({"message": "cannot update color scheme without a valid uuid"}), 400

    color_scheme_query = db.session.query(ColorSchemes).filter(ColorSchemes.color_scheme_id == color_scheme_id).first()
    return record_delete_by_id(color_scheme_query, "color_scheme")