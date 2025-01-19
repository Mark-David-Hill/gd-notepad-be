from flask import jsonify

from db import db
from models.collections import Collections, collection_schema, collections_schema
from util.controllers_util import *
from lib.authenticate import auth, authenticate_return_auth, validate_uuid4


@authenticate_return_auth
def collection_add(req, auth_info):
    user_id = str(auth_info.user.user_id)

    collection = Collections.new_collection_obj()
    collection.owner_id = user_id

    return record_add(req, collection, collection_schema, "collection")
    
    
# @auth
def collections_get_all():
    return records_get_all(Collections, collections_schema, "collections")


# @auth
def collection_get_by_id(collection_id):
    if not validate_uuid4(collection_id):
        return jsonify({"message": f"cannot get collection without a valid uuid"}), 400
    
    collection_query = db.session.query(Collections).filter(Collections.collection_id == collection_id).first()
    return record_get_by_id(collection_query, collection_schema, "collection")


@authenticate_return_auth
def collection_update_by_id(req, collection_id, auth_info):
    if not validate_uuid4(collection_id):
        return jsonify({"message": "cannot update collection without a valid uuid"}), 400

    user_id = str(auth_info.user.user_id)

    collection_query = db.session.query(Collections).filter(Collections.collection_id == collection_id).first()

    if collection_query:
        # Check if the logged-in user is the owner of the collection
        # if collection_query.owner_id != user_id and auth_info.user.role != 'super-admin':
        #     return jsonify({"message": "You can only update collections that you own."}), 403
        
        # Proceed with the update
        return record_update_by_id(req, collection_query, collection_schema, "collection")

    return jsonify({"message": "Collection not found"}), 404


@auth
def collection_delete_by_id(collection_id):
    if not validate_uuid4(collection_id):
        return jsonify({"message": "cannot update collection without a valid uuid"}), 400

    collection_query = db.session.query(Collections).filter(Collections.collection_id == collection_id).first()
    return record_delete_by_id(collection_query, "collection")