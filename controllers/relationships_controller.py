from flask import jsonify

from db import db
from models.relationships import Relationships, relationship_schema, relationships_schema
from models.items import Items
from util.controllers_util import *
from lib.authenticate import auth, validate_uuid4


@auth
def relationship_add(req):
    post_data = req.form if req.form else req.json
    if not validate_uuid4(post_data.get("item_1_id")) or not validate_uuid4(post_data.get("item_2_id")):
        return jsonify({"message": "could not create relationship, must provide valid uuids for both items"}), 400
    
    item_1_query = db.session.query(Items).filter(Items.item_id == post_data.get("item_1_id")).first()
    item_2_query = db.session.query(Items).filter(Items.item_id == post_data.get("item_2_id")).first()
    if  not item_1_query or not item_2_query:
        return jsonify({"message": "could not create relationship, at least one of these items does not exist"})
    
    return record_add(req, Relationships.new_relationship_obj(), relationship_schema, "relationship")
    

# @auth
def relationships_get_all():
    return records_get_all(Relationships, relationships_schema, "relationships")


def relationships_get_by_collection(collection_id):
    # Use joinedload to eagerly load the related items
    from sqlalchemy.orm import joinedload
    relationships_query = db.session.query(Relationships).options(
        joinedload(Relationships.item_1),
        joinedload(Relationships.item_2)
    ).filter(Relationships.collection_id == collection_id).all()
    
    if not relationships_query:
        return jsonify({"message": "No relationships found for the given collection"}), 404
    
    return jsonify({
        "message": "relationships found",
        "results": relationships_schema.dump(relationships_query)
    }), 200


# @auth
def relationship_get_by_id(relationship_id):
    if not validate_uuid4(relationship_id):
        return jsonify({"message": "cannot get relationship without a valid uuid"}), 400

    relationship_query = db.session.query(Relationships).filter(Relationships.relationship_id == relationship_id).first()
    return record_get_by_id(relationship_query, relationship_schema, "relationship")


@auth
def relationship_update_by_id(req, relationship_id):
    if not validate_uuid4(relationship_id):
        return jsonify({"message": "cannot update relationship without a valid uuid"}), 400

    relationship_query = db.session.query(Relationships).filter(Relationships.relationship_id == relationship_id).first()
    return record_update_by_id(req, relationship_query, relationship_schema, "relationship")


@auth
def relationship_delete_by_id(relationship_id):
    if not validate_uuid4(relationship_id):
        return jsonify({"message": "cannot update relationship without a valid uuid"}), 400

    relationship_query = db.session.query(Relationships).filter(Relationships.relationship_id == relationship_id).first()
    return record_delete_by_id(relationship_query, "relationship")