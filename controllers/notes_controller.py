from flask import jsonify
from datetime import datetime

from db import db
from models.notes import Notes, note_schema, notes_schema
from util.reflection import populate_object
from util.controllers_util import *
from lib.authenticate import auth, validate_uuid4


@auth
def note_add(req):
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
        