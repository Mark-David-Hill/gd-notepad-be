from flask import jsonify

from db import db
from models.notes import Notes, note_schema, notes_schema
from models.users import Users
from models.items import Items
from util.controllers_util import *
from lib.authenticate import auth, validate_uuid4


@auth
def note_add(req):
    post_data = req.form if req.form else req.json
    if not validate_uuid4(post_data.get("user_id")) or not validate_uuid4(post_data.get("item_id")):
        return jsonify({"message": "could not create note, must provide valid uuids for user id and item id"}), 400
    
    user_query = db.session.query(Users).filter(Users.user_id == post_data.get("user_id")).first()
    if  not user_query:
        return jsonify({"message": "could not create note, user does not exist"})
    
    item_query = db.session.query(Items).filter(Items.item_id == post_data.get("item_id")).first()
    if  not item_query:
        return jsonify({"message": "could not create note, item does not exist"})

    return record_add(req, Notes.new_note_obj(), note_schema, "note", True)
    

@auth
def notes_get_all():
    return records_get_all(Notes, notes_schema, "notes")


@auth
def note_get_by_id(note_id):
    if not validate_uuid4(note_id):
        return jsonify({"message": "cannot get note without a valid uuid"}), 400

    note_query = db.session.query(Notes).filter(Notes.note_id == note_id).first()
    return record_get_by_id(note_query, note_schema, "note")


@auth
def note_update_by_id(req, note_id):
    if not validate_uuid4(note_id):
        return jsonify({"message": "cannot update note without a valid uuid"}), 400

    note_query = db.session.query(Notes).filter(Notes.note_id == note_id).first()
    return record_update_by_id(req, note_query, note_schema, "note")


@auth
def note_delete_by_id(note_id):
    if not validate_uuid4(note_id):
        return jsonify({"message": "cannot update note without a valid uuid"}), 400

    note_query = db.session.query(Notes).filter(Notes.note_id == note_id).first()
    return record_delete_by_id(note_query, "note")
        