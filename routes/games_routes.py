from flask import Blueprint, request

import controllers

games = Blueprint("game", __name__)


@games.route("/game", methods=["POST"])
def game_add():
    return controllers.game_add(request)


@games.route("/games")
def games_get_all():
    return controllers.games_get_all()


@games.route("/game/<game_id>")
def game_get_by_id(game_id):
    return controllers.game_get_by_id(game_id)


@games.route("/game/<game_id>", methods=["PUT"])
def game_update_by_id(game_id):
    return controllers.game_update_by_id(request, game_id)


@games.route("/game/<game_id>", methods=["DELETE"])
def game_delete_by_id(game_id):
    return controllers.game_delete_by_id(game_id)
