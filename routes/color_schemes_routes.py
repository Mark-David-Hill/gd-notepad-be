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


# @items.route("/item/<item_id>", methods=["PUT"])
# def item_update_by_id(item_id):
#     return controllers.item_update_by_id(request, item_id)


# @items.route("/item/delete/<item_id>", methods=["DELETE"])
# def item_delete_by_id(item_id):
#     return controllers.item_delete_by_id(item_id)
