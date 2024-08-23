from flask import jsonify

from db import db
from models.element_relationships import ElementRelationships, relationship_schema, relationships_schema
from models.game_elements import GameElements
from util.controllers_util import *
from lib.authenticate import auth, validate_uuid4


@auth
def relationship_add(req):
    post_data = req.form if req.form else req.json
    if not validate_uuid4(post_data.get("element_1_id")) or not validate_uuid4(post_data.get("element_2_id")):
        return jsonify({"message": "could not create relationship, must provide valid uuids for both elements"}), 400
    
    element_1_query = db.session.query(GameElements).filter(GameElements.element_id == post_data.get("element_1_id")).first()
    element_2_query = db.session.query(GameElements).filter(GameElements.element_id == post_data.get("element_2_id")).first()
    if  not element_1_query or not element_2_query:
        return jsonify({"message": "could not create relationship, at least one of these elements does not exist"})
    
    return record_add(req, ElementRelationships.new_relationship_obj(), relationship_schema, "relationship")
    

@auth
def relationships_get_all():
    return records_get_all(ElementRelationships, relationships_schema, "relationships")


@auth
def relationship_get_by_id(relationship_id):
    if not validate_uuid4(relationship_id):
        return jsonify({"message": "cannot get relationship without a valid uuid"}), 400

    relationship_query = db.session.query(ElementRelationships).filter(ElementRelationships.relationship_id == relationship_id).first()
    return record_get_by_id(relationship_query, relationship_schema, "relationship")


@auth
def relationship_update_by_id(req, relationship_id):
    if not validate_uuid4(relationship_id):
        return jsonify({"message": "cannot update relationship without a valid uuid"}), 400

    relationship_query = db.session.query(ElementRelationships).filter(ElementRelationships.relationship_id == relationship_id).first()
    return record_update_by_id(req, relationship_query, relationship_schema, "relationship")


@auth
def relationship_delete_by_id(relationship_id):
    if not validate_uuid4(relationship_id):
        return jsonify({"message": "cannot update relationship without a valid uuid"}), 400

    relationship_query = db.session.query(ElementRelationships).filter(ElementRelationships.relationship_id == relationship_id).first()
    return record_delete_by_id(relationship_query, "relationship")