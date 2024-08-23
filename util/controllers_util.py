from flask import jsonify
from flask_bcrypt import generate_password_hash
from datetime import datetime

from db import db
from util.reflection import populate_object


def record_add(req, new_record_obj, schema, record_type, needs_datetime=False, needs_password=False):
    post_data = req.form if req.form else req.json

    if not post_data:
        return jsonify({"message": "all required fields must be submitted"}), 400
    
    new_record = new_record_obj

    populate_object(new_record, post_data)

    if needs_datetime:
        new_record.date_time = datetime.now()

    if needs_password:
        new_record.password = generate_password_hash(new_record.password).decode('utf8')

    db.session.add(new_record)
    db.session.commit()
    return jsonify({"message": f"{record_type} created", "result": schema.dump(new_record)}), 201


def records_get_all(table, schema, records_type_str):
    records_query = db.session.query(table).all()

    if not records_query:
        return jsonify({"message": f"no {records_type_str} found"}), 404
    
    return jsonify({"message": f"{records_type_str} found", "results": schema.dump(records_query)}), 200


def record_get_by_id(record_query, schema, record_type_str):
    if not record_query:
        return jsonify({"message": f"{record_type_str} does not exist"}), 404

    return jsonify({"message": f"{record_type_str} found", "result": schema.dump(record_query)}), 200


def record_update_by_id(req, record_query, schema, record_type_str):
    post_data = req.form if req.form else req.json

    populate_object(record_query, post_data)

    if not record_query:
        return jsonify({"message": f"{record_type_str} does not exist"}), 404
    
    db.session.commit()
    return jsonify({"message": f"{record_type_str} updated", "result": schema.dump(record_query)}), 201


def record_delete_by_id(record_query, record_type_str):

    if not record_query:
        return jsonify({"message": f"{record_type_str} does not exist"}), 404
    
    try:
        db.session.delete(record_query)
        db.session.commit()
        return jsonify({"message": f"the {record_type_str} was deleted"}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": f"could not delete {record_type_str}"}), 400