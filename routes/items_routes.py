from flask import Blueprint, request

import controllers

items = Blueprint("item", __name__)


@items.route("/item", methods=["POST"])
def item_add():
    return controllers.item_add(request)


@items.route("/item/tag", methods=["POST"])
def item_tag_update():
    return controllers.item_tag_update(request)


@items.route("/items")
def items_get_all():
    return controllers.items_get_all()


@items.route("/items/tag/<tag_id>")
def items_get_all_with_tag(tag_id):
    return controllers.items_get_all_with_tag(tag_id)


@items.route("/item/<item_id>")
def item_get_by_id(item_id):
    return controllers.item_get_by_id(item_id)


@items.route("/item/<item_id>", methods=["PUT"])
def item_update_by_id(item_id):
    return controllers.item_update_by_id(request, item_id)


@items.route("/item/delete/<item_id>", methods=["DELETE"])
def item_delete_by_id(item_id):
    return controllers.item_delete_by_id(item_id)
