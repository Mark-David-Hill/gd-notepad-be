from flask import jsonify, request, make_response
from flask_bcrypt import check_password_hash
from datetime import datetime, timedelta, timezone

from db import db
from models.app_users import AppUsers, app_user_schema
from models.auth_tokens import AuthTokens, auth_token_schema


def auth_token_add(req):
    post_data = req.form if req.form else req.json

    email = post_data.get("email")
    password = post_data.get("password")

    if email and password:
        user_data = db.session.query(AppUsers).filter(AppUsers.email == post_data.get("email")).first()

        if user_data:
            valid_password = check_password_hash(user_data.password, password)

            if not valid_password:
                return jsonify({"message": "invalid login"}), 401
            
            existing_tokens = db.session.query(AuthTokens).filter(AuthTokens.user_id == user_data.user_id).all()

            if existing_tokens:
                for token in existing_tokens:
                    if token.expiration < datetime.now(timezone.utc):
                        db.session.delete(token)

            expiry = datetime.now(timezone.utc) + timedelta(hours=12)

            new_token = AuthTokens(user_data.user_id, expiry)
            db.session.add(new_token)
            db.session.commit()

            response = make_response(jsonify({"message": "login successful", "result": app_user_schema.dump(user_data)}), 201)
            response.set_cookie("_sid", str(new_token.auth_token), httponly=True, secure=False)
            # samesite="None"
            return response
        else:
            return jsonify({"message": "no user data found"}), 404

    else:
        return jsonify({"message": "email and password are required fields"}), 400
    
# def logout(self, auth_info):
#     auth_data = db.session.query(AuthTokens).filter(AppUsers.email == post_data.get("email")).first()

# def check_login(self, auth_info):
#     user_data = db.session.query(AppUsers).filter(AppUsers.email == post_data.get("email")).first()