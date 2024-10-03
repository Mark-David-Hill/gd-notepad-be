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
            # response.set_cookie("_sid", str(new_token.auth_token), httponly=True, secure=False)
            response.set_cookie("_sid", str(new_token.auth_token), httponly=True, secure=False, samesite='Strict')
            # samesite="None"
            return response
        else:
            return jsonify({"message": "no user data found"}), 404

    else:
        return jsonify({"message": "email and password are required fields"}), 400
    

# def check_login(req):
#     # Get the _sid cookie from the request
#     auth_token = request.cookies.get('_sid')

#     if not auth_token:
#         # If the _sid cookie doesn't exist, the user is not logged in
#         return jsonify({"message": "not authenticated"}), 401

#     # Query the database for the token
#     token_data = db.session.query(AuthTokens).filter_by(auth_token=auth_token).first()

#     if not token_data:
#         # No token found for the given _sid
#         return jsonify({"message": "invalid token"}), 401

#     # Check if the token is expired
#     if token_data.expiration < datetime.now(timezone.utc):
#         # Token is expired
#         return jsonify({"message": "token expired"}), 401

#     # If the token is valid, return success with the auth token
#     return jsonify({
#         "message": "authenticated", 
#         "user_id": token_data.user_id,
#         "auth_token": token_data.auth_token  # Include the token in the response
#     }), 200

    # post_data = req.form if req.form else req.json
    # user_id = post_data.get('user_id')

    # if not user_id:
    #     return jsonify({"message": "user_id is a required field"})

    # existing_tokens = db.session.query(AuthTokens).filter(AuthTokens.user_id == user_id).all()

    # if existing_tokens:
    #     try:
    #         for token in existing_tokens:
    #             db.session.delete(token)

    #         db.session.commit()
    #         return ({"message": f"user with id {user_id} has been logged out"})
    #     except:
    #         db.session.rollback()
    #         return jsonify({"message": f"unable to logout user with id {user_id}"}), 400
    # else:
    #     return jsonify({"message": f"user with id {user_id} has been logged out"})


# def logout(self, auth_info):
#     auth_data = db.session.query(AuthTokens).filter(AppUsers.email == post_data.get("email")).first()

# def check_login(self, auth_info):
#     user_data = db.session.query(AppUsers).filter(AppUsers.email == post_data.get("email")).first()