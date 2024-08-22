from flask import jsonify
from uuid import UUID

from db import db
from models.games import Games, game_schema, games_schema
from util.reflection import populate_object
from lib.authenticate import auth, validate_uuid4


@auth
def game_add(req):
    post_data = req.form if req.form else req.json

    if not post_data:
        return jsonify({"message": "all required fields must be submitted"}), 400
    
    new_game = Games.new_game_obj()

    populate_object(new_game, post_data)

    try:
        db.session.add(new_game)
        db.session.commit()
        return jsonify({"message": "game created", "result": game_schema.dump(new_game)}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not create game"}), 400
    
    
@auth
def games_get_all():
    games_query = db.session.query(Games).all()

    if not games_query:
        return jsonify({"message": "no games found"}), 404
    
    return jsonify({"message": "games found", "results": games_schema.dump(games_query)}), 200


@auth
def game_get_by_id(game_id):
    if not validate_uuid4(game_id):
        return jsonify({"message": "cannot get game without a valid uuid"}), 400

    game_query = db.session.query(Games).filter(Games.game_id == game_id).first()

    if not game_query:
        return jsonify({"message": "game does not exist"}), 404
    
    return jsonify({"message": "game found", "result": game_schema.dump(game_query)}), 200


@auth
def game_update_by_id(req, game_id):
    post_data = req.form if req.form else req.json

    if not validate_uuid4(game_id):
        return jsonify({"message": "cannot update game without a valid uuid"}), 400

    game_query = db.session.query(Games).filter(Games.game_id == game_id).first()

    populate_object(game_query, post_data)

    if not game_query:
        return jsonify({"message": "game does not exist"}), 404
    
    try:
        db.session.commit()
        return jsonify({"message": "game updated", "result": game_schema.dump(game_query)}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not update game"}), 400


@auth
def game_delete_by_id(game_id):
    if not validate_uuid4(game_id):
        return jsonify({"message": "cannot update game without a valid uuid"}), 400

    game_query = db.session.query(Games).filter(Games.game_id == game_id).first()

    if not game_query:
        return jsonify({"message": "game does not exist"}), 404
    
    try:
        db.session.delete(game_query)
        db.session.commit()
        return jsonify({"message": "the game was deleted"}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not delete game"}), 400
        