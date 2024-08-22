from flask import jsonify
from uuid import UUID

from db import db
from models.element_relationships import ElementRelationships, relationship_schema, relationships_schema
from util.reflection import populate_object
from lib.authenticate import auth


@auth
def relationship_add(req):
    post_data = req.form if req.form else req.json

    if not post_data:
        return jsonify({"message": "all required fields must be submitted"})
    
    print("POST DATA", post_data)
    
    new_relationship = ElementRelationships.new_relationship_obj()

    populate_object(new_relationship, post_data)

    try:
        db.session.add(new_relationship)
        db.session.commit()
        return jsonify({"message": "relationship created", "result": relationship_schema.dump(new_relationship)}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not create relationship"})
    

@auth
def relationships_get_all():
    relationships_query = db.session.query(ElementRelationships).all()

    if not relationships_query:
        return jsonify({"message": "no relationships found"}), 404
    
    return jsonify({"message": "relationships found", "results": relationships_schema.dump(relationships_query)}), 200


@auth
def relationship_get_by_id(relationship_id):
    try:
        UUID(relationship_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot get relationship without a valid uuid"})

    relationship_query = db.session.query(ElementRelationships).filter(ElementRelationships.relationship_id == relationship_id).first()

    if not relationship_query:
        return jsonify({"message": "relationship does not exist"}), 404
    
    return jsonify({"message": "relationship found", "result": relationship_schema.dump(relationship_query)}), 200


@auth
def relationship_update_by_id(req, relationship_id):
    post_data = req.form if req.form else req.json

    try:
        UUID(relationship_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot update relationship without a valid uuid"})

    relationship_query = db.session.query(ElementRelationships).filter(ElementRelationships.relationship_id == relationship_id).first()

    populate_object(relationship_query, post_data)

    if not relationship_query:
        return jsonify({"message": "relationship does not exist"}), 404
    
    try:
        db.session.commit()
        return jsonify({"message": "relationship updated", "result": relationship_schema.dump(relationship_query)}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not update relationship"})


@auth
def relationship_delete_by_id(relationship_id):
    try:
        UUID(relationship_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot update relationship without a valid uuid"})

    relationship_query = db.session.query(ElementRelationships).filter(ElementRelationships.relationship_id == relationship_id).first()

    if not relationship_query:
        return jsonify({"message": "relationship does not exist"}), 404
    
    try:
        db.session.delete(relationship_query)
        db.session.commit()
        return jsonify({"message": "the relationship was deleted"}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not delete relationship"})
        