from flask import jsonify
from flask_bcrypt import generate_password_hash
from uuid import UUID

from db import db
from models.app_users import AppUsers, app_user_schema, app_users_schema
from util.reflection import populate_object
from lib.authenticate import auth


def user_add(req):
    post_data = req.form if req.form else req.json

    if not post_data:
        return jsonify({"message": "all required fields must be submitted"}), 400
    
    new_user = AppUsers.new_user_obj()

    populate_object(new_user, post_data)

    new_user.password = generate_password_hash(new_user.password).decode('utf8')

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "user created", "result": app_user_schema.dump(new_user)}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not create user"}), 400
    
    

def users_get_all():
    users_query = db.session.query(AppUsers).all()

    if not users_query:
        return jsonify({"message": "no users found"}), 404
    
    return jsonify({"message": "users found", "results": app_users_schema.dump(users_query)}), 200


@auth
def user_get_by_id(user_id):
    try:
        UUID(user_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot get user without a valid uuid"}), 400

    user_query = db.session.query(AppUsers).filter(AppUsers.user_id == user_id).first()

    if not user_query:
        return jsonify({"message": "user does not exist"}), 404
    
    return jsonify({"message": "user found", "result": app_user_schema.dump(user_query)}), 200


@auth
def user_update_by_id(req, user_id):
    post_data = req.form if req.form else req.json

    try:
        UUID(user_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot update user without a valid uuid"}), 400

    user_query = db.session.query(AppUsers).filter(AppUsers.user_id == user_id).first()

    populate_object(user_query, post_data)

    if not user_query:
        return jsonify({"message": "user does not exist"}), 404
    
    try:
        db.session.commit()
        return jsonify({"message": "user updated", "result": app_user_schema.dump(user_query)}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not update user"}), 400


@auth
def user_delete_by_id(user_id):
    try:
        UUID(user_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot update user without a valid uuid"}), 400

    user_query = db.session.query(AppUsers).filter(AppUsers.user_id == user_id).first()

    if not user_query:
        return jsonify({"message": "user does not exist"}), 404
    
    try:
        db.session.delete(user_query)
        db.session.commit()
        return jsonify({"message": "the user was deleted", "result": app_user_schema.dump(user_query)}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not delete user"}), 400
        