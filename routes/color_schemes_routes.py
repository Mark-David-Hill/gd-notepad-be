from flask import Blueprint, request

import controllers

color_schemes = Blueprint("color_scheme", __name__)


@color_schemes.route("/color-scheme", methods=["POST"])
def color_scheme_add():
    return controllers.color_scheme_add(request)


@color_schemes.route("/color-schemes")
def color_schemes_get_all():
    return controllers.color_schemes_get_all()


@color_schemes.route("/color_scheme/<color_scheme_id>")
def color_scheme_get_by_id(color_scheme_id):
    return controllers.color_scheme_get_by_id(color_scheme_id)


@color_schemes.route("/color_scheme/<color_scheme_id>", methods=["PUT"])
def color_scheme_update_by_id(color_scheme_id):
    return controllers.color_scheme_update_by_id(request, color_scheme_id)


@color_schemes.route("/color_scheme/delete/<color_scheme_id>", methods=["DELETE"])
def color_scheme_delete_by_id(color_scheme_id):
    return controllers.color_scheme_delete_by_id(color_scheme_id)
