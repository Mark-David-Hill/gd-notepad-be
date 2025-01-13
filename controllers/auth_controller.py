from flask import jsonify, request, make_response
from flask_bcrypt import check_password_hash
from datetime import datetime, timedelta, timezone

from db import db
from models.users import Users, user_schema
from models.auth_tokens import AuthTokens


def auth_token_add(req):
    post_data = req.form if req.form else req.json

    email = post_data.get("email")
    password = post_data.get("password")

    if email and password:
        user_data = db.session.query(Users).filter(Users.email == post_data.get("email")).first()

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

            response = make_response(jsonify({"message": "login successful", "result": user_schema.dump(user_data)}), 201)
            response.set_cookie("_sid", str(new_token.auth_token), httponly=True, secure=False, samesite='Strict')
            # samesite="None"
            return response
        else:
            return jsonify({"message": "no user data found"}), 404

    else:
        return jsonify({"message": "email and password are required fields"}), 400
    

def check_login():
    token = request.cookies.get("_sid")

    if not token:
        return jsonify({"message": "No session token found"}), 401

    auth_token_data = db.session.query(AuthTokens).filter(AuthTokens.auth_token == token).first()

    if auth_token_data and auth_token_data.expiration > datetime.now(timezone.utc):
        user_data = db.session.query(Users).filter(Users.user_id == auth_token_data.user_id).first()

        if user_data:
            return jsonify({"message": "User is logged in", "result": user_schema.dump(user_data)}), 200
        else:
            return jsonify({"message": "User not found"}), 404
    else:
        return jsonify({"message": "Invalid or expired session token"}), 401


# def logout(self, auth_info):
#     auth_data = db.session.query(AuthTokens).filter(Users.email == post_data.get("email")).first()