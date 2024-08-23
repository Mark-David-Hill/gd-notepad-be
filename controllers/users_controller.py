from flask import jsonify
from flask_bcrypt import generate_password_hash
from uuid import UUID

from db import db
from models.app_users import AppUsers, app_user_schema, app_users_schema
from util.reflection import populate_object
from util.controllers_util import record_add, records_get_all
from lib.authenticate import auth, validate_uuid4, authenticate_return_auth


def user_add(req):
    return record_add(req, AppUsers.new_user_obj(), app_user_schema, "user", True)
    
    
@auth
def users_get_all():
    return records_get_all(AppUsers, app_users_schema, "users")


@authenticate_return_auth
def user_get_by_id(req, user_id, auth_info):
    if not validate_uuid4(user_id):
        return jsonify({"message": "cannot get user without a valid uuid"}), 400

    user_query = db.session.query(AppUsers).filter(AppUsers.user_id == user_id).first()

    if user_id == str(auth_info.user.user_id) or auth_info.user.role == 'super-admin':
        if not user_query:
            return jsonify({"message": "user does not exist"}), 404
        return jsonify({"message": "user found", "result": app_user_schema.dump(user_query)}), 200
    else:
        return jsonify({"message": "unauthorized"}), 403


@authenticate_return_auth
def user_update_by_id(req, user_id, auth_info):
    post_data = req.form if req.form else req.json

    if not validate_uuid4(user_id):
        return jsonify({"message": "cannot update user without a valid uuid"}), 400

    user_query = db.session.query(AppUsers).filter(AppUsers.user_id == user_id).first()

    populate_object(user_query, post_data)

    if user_id == str(auth_info.user.user_id) or auth_info.user.role == 'super-admin':
        if not user_query:
            return jsonify({"message": "user does not exist"}), 404
        db.session.commit()
        return jsonify({"message": "user updated", "result": app_user_schema.dump(user_query)}), 201
    else:
        return jsonify({"message": "unauthorized"}), 403


@authenticate_return_auth
def user_delete_by_id(req, user_id, auth_info):
    if not validate_uuid4(user_id):
        return jsonify({"message": "cannot update user without a valid uuid"}), 400

    user_query = db.session.query(AppUsers).filter(AppUsers.user_id == user_id).first()

    if user_id == str(auth_info.user.user_id) or auth_info.user.role == 'super-admin':
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
    else:
        return jsonify({"message": "unauthorized"}), 403
        