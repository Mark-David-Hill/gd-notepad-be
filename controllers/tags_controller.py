from flask import jsonify

from db import db
from models.tags import Tags, tag_schema, tags_schema
from util.reflection import populate_object
from util.controllers_util import *
from lib.authenticate import auth, validate_uuid4


@auth
def tag_add(req):
    return record_add(req, Tags.new_tag_obj(), tag_schema, "tag")
    
    
@auth
def tags_get_all():
    return records_get_all(Tags, tags_schema, "tags")


@auth
def tag_get_by_id(tag_id):
    if not validate_uuid4(tag_id):
        return jsonify({"message": "cannot get tag without a valid uuid"}), 400

    tag_query = db.session.query(Tags).filter(Tags.tag_id == tag_id).first()
    return record_get_by_id(tag_query, tag_schema, "tag")


@auth
def tag_update_by_id(req, tag_id):
    if not validate_uuid4(tag_id):
        return jsonify({"message": "cannot update tag without a valid uuid"}), 400

    tag_query = db.session.query(Tags).filter(Tags.tag_id == tag_id).first()
    return record_update_by_id(req, tag_query, tag_schema, "tag")


@auth
def tag_delete_by_id(tag_id):
    if not validate_uuid4(tag_id):
        return jsonify({"message": "cannot update tag without a valid uuid"}), 400

    tag_query = db.session.query(Tags).filter(Tags.tag_id == tag_id).first()
    return record_delete_by_id(tag_query, "tag")
        