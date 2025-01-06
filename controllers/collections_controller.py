from flask import jsonify

from db import db
from models.collections import Collections, collection_schema, collections_schema
from util.controllers_util import *
from lib.authenticate import auth, validate_uuid4


@auth
def collection_add(req):
    return record_add(req, Collections.new_collection_obj(), collection_schema, "collection")
    
    
# @auth
def collections_get_all():
    return records_get_all(Collections, collections_schema, "collections")


# @auth
def collection_get_by_id(collection_id):
    if not validate_uuid4(collection_id):
        return jsonify({"message": f"cannot get collection without a valid uuid"}), 400
    
    collection_query = db.session.query(Collections).filter(Collections.collection_id == collection_id).first()
    return record_get_by_id(collection_query, collection_schema, "collection")


@auth
def collection_update_by_id(req, collection_id):
    if not validate_uuid4(collection_id):
        return jsonify({"message": "cannot update collection without a valid uuid"}), 400

    collection_query = db.session.query(Collections).filter(Collections.collection_id == collection_id).first()
    return record_update_by_id(req, collection_query, collection_schema, "collection")


@auth
def collection_delete_by_id(collection_id):
    if not validate_uuid4(collection_id):
        return jsonify({"message": "cannot update collection without a valid uuid"}), 400

    collection_query = db.session.query(Collections).filter(Collections.collection_id == collection_id).first()
    return record_delete_by_id(collection_query, "collection")