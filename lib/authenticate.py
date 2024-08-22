from flask import jsonify, request
import functools
from datetime import datetime
from uuid import UUID

from db import db
from models.auth_tokens import AuthTokens
from models.app_users import AppUsers


def validate_uuid4(uuid_string):
    try:
        UUID(uuid_string, version=4)
        return True
    except Exception as e:
        print("error validating uuid4", e)
        return False
    

def validate_token(req):
    auth_token = req.headers.get("auth")

    if not auth_token or not validate_uuid4(auth_token):
        print("error, could not validate auth token")
        return False
    
    existing_token = db.session.query(AuthTokens).filter(AuthTokens.auth_token == auth_token).first()

    if existing_token:
        if existing_token.expiration > datetime.now():
            return existing_token
    else:
        print("no auth token found")
        return False
    

def fail_response():
    return jsonify({"message": "authentication required"}), 401


def auth(function):
    @functools.wraps(function)
    def function_wrapper(*args, **kwargs):
        auth_info = validate_token(request)

        if auth_info:
            return function(*args, **kwargs)
        else:
            return fail_response()
        
    return function_wrapper


def authenticate_return_auth(func):
  @functools.wraps(func)
  def wrapper_authenticate(*args, **kwargs):
    auth_info = validate_token(args[0])
    kwargs["auth_info"] = auth_info

    return(
      func(
        *args, **kwargs
        ) if auth_info else fail_response()
    )
  
  return wrapper_authenticate