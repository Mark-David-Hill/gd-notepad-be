from flask import jsonify
from uuid import UUID
from datetime import datetime

from db import db
from models.notes import Notes, note_schema, notes_schema
from util.reflection import populate_object
from lib.authenticate import auth, validate_uuid4


@auth
def note_add(req):
    post_data = req.form if req.form else req.json

    if not post_data:
        return jsonify({"message": "all required fields must be submitted"}), 400
    
    new_note = Notes.new_note_obj()

    populate_object(new_note, post_data)

    new_note.date_time = datetime.now()

    db.session.add(new_note)
    db.session.commit()
    return jsonify({"message": "note created", "result": note_schema.dump(new_note)}), 201
    

@auth
def notes_get_all():
    notes_query = db.session.query(Notes).all()

    if not notes_query:
        return jsonify({"message": "no notes found"}), 404
    
    return jsonify({"message": "notes found", "results": notes_schema.dump(notes_query)}), 200


@auth
def note_get_by_id(note_id):
    if not validate_uuid4(note_id):
        return jsonify({"message": "cannot get note without a valid uuid"}), 400

    note_query = db.session.query(Notes).filter(Notes.note_id == note_id).first()

    if not note_query:
        return jsonify({"message": "note does not exist"}), 404
    
    return jsonify({"message": "note found", "result": note_schema.dump(note_query)}), 200


@auth
def note_update_by_id(req, note_id):
    post_data = req.form if req.form else req.json

    if not validate_uuid4(note_id):
        return jsonify({"message": "cannot update note without a valid uuid"}), 400

    note_query = db.session.query(Notes).filter(Notes.note_id == note_id).first()

    populate_object(note_query, post_data)

    if not note_query:
        return jsonify({"message": "note does not exist"}), 404
    
    db.session.commit()
    return jsonify({"message": "note updated", "result": note_schema.dump(note_query)}), 201


@auth
def note_delete_by_id(note_id):
    if not validate_uuid4(note_id):
        return jsonify({"message": "cannot update note without a valid uuid"}), 400

    note_query = db.session.query(Notes).filter(Notes.note_id == note_id).first()

    if not note_query:
        return jsonify({"message": "note does not exist"}), 404
    
    try:
        db.session.delete(note_query)
        db.session.commit()
        return jsonify({"message": "the note was deleted"}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not delete note"}), 400
        