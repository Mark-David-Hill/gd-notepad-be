from flask import jsonify

from db import db
from models.games import Games, game_schema, games_schema
from util.controllers_util import *
from lib.authenticate import auth, validate_uuid4


@auth
def game_add(req):
    return record_add(req, Games.new_game_obj(), game_schema, "game")
    
    
@auth
def games_get_all():
    return records_get_all(Games, games_schema, "games")


@auth
def game_get_by_id(game_id):
    if not validate_uuid4(game_id):
        return jsonify({"message": f"cannot get game without a valid uuid"}), 400
    
    game_query = db.session.query(Games).filter(Games.game_id == game_id).first()
    return record_get_by_id(game_query, game_schema, "game")


@auth
def game_update_by_id(req, game_id):
    if not validate_uuid4(game_id):
        return jsonify({"message": "cannot update game without a valid uuid"}), 400

    game_query = db.session.query(Games).filter(Games.game_id == game_id).first()
    return record_update_by_id(req, game_query, game_schema, "game")


@auth
def game_delete_by_id(game_id):
    if not validate_uuid4(game_id):
        return jsonify({"message": "cannot update game without a valid uuid"}), 400

    game_query = db.session.query(Games).filter(Games.game_id == game_id).first()
    return record_delete_by_id(game_query, "game")