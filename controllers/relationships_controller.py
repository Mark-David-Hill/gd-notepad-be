from flask import jsonify

from db import db
from models.element_relationships import ElementRelationships, relationship_schema, relationships_schema
from util.reflection import populate_object
from util.controllers_util import *
from lib.authenticate import auth, validate_uuid4


@auth
def relationship_add(req):
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