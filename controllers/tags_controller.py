from flask import jsonify
from uuid import UUID

from db import db
from models.tags import Tags, tag_schema, tags_schema
from util.reflection import populate_object
from lib.authenticate import auth


@auth
def tag_add(req):
    post_data = req.form if req.form else req.json

    if not post_data:
        return jsonify({"message": "all required fields must be submitted"})
    
    new_tag = Tags.new_tag_obj()

    populate_object(new_tag, post_data)

    try:
        db.session.add(new_tag)
        db.session.commit()
        return jsonify({"message": "tag created", "result": tag_schema.dump(new_tag)}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not create tag"})
    
    
@auth
def tags_get_all():
    tags_query = db.session.query(Tags).all()

    if not tags_query:
        return jsonify({"message": "no tags found"}), 404
    
    return jsonify({"message": "tags found", "results": tags_schema.dump(tags_query)}), 200


@auth
def tag_get_by_id(tag_id):
    try:
        UUID(tag_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot get tag without a valid uuid"})

    tag_query = db.session.query(Tags).filter(Tags.tag_id == tag_id).first()

    if not tag_query:
        return jsonify({"message": "tag does not exist"}), 404
    
    return jsonify({"message": "tag found", "result": tag_schema.dump(tag_query)}), 200


@auth
def tag_update_by_id(req, tag_id):
    post_data = req.form if req.form else req.json

    try:
        UUID(tag_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot update tag without a valid uuid"})

    tag_query = db.session.query(Tags).filter(Tags.tag_id == tag_id).first()

    populate_object(tag_query, post_data)

    if not tag_query:
        return jsonify({"message": "tag does not exist"}), 404
    
    try:
        db.session.commit()
        return jsonify({"message": "tag updated", "result": tag_schema.dump(tag_query)}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not update tag"})


@auth
def tag_delete_by_id(tag_id):
    try:
        UUID(tag_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot update tag without a valid uuid"})

    tag_query = db.session.query(Tags).filter(Tags.tag_id == tag_id).first()

    if not tag_query:
        return jsonify({"message": "tag does not exist"}), 404
    
    try:
        db.session.delete(tag_query)
        db.session.commit()
        return jsonify({"message": "the tag was deleted"}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not delete tag"})
        