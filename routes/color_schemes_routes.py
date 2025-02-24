from flask import Blueprint, request

import controllers

color_schemes = Blueprint("color_scheme", __name__)


# @color_schemes.route("/color-scheme", methods=["POST"])
# def color_scheme_add():
#     return controllers.color_scheme_add(request)


# @color_schemes.route("/item/tag", methods=["POST"])
# def item_tag_update():
#     return controllers.item_tag_update(request)


@color_schemes.route("/color-schemes")
def color_schemes_get_all():
    return controllers.color_schemes_get_all()


# @items.route("/items/collection/<collection_id>")
# def items_get_by_collection(collection_id):
#     return controllers.items_get_by_collection(collection_id)


# @items.route("/items/tag/<tag_id>")
# def items_get_all_with_tag(tag_id):
#     return controllers.items_get_all_with_tag(tag_id)


# @items.route("/item/<item_id>")
# def item_get_by_id(item_id):
#     return controllers.item_get_by_id(item_id)


# @items.route("/item/<item_id>", methods=["PUT"])
# def item_update_by_id(item_id):
#     return controllers.item_update_by_id(request, item_id)


# @items.route("/item/delete/<item_id>", methods=["DELETE"])
# def item_delete_by_id(item_id):
#     return controllers.item_delete_by_id(item_id)
