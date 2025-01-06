from flask import Blueprint, request

import controllers

collections = Blueprint("collection", __name__)


@collections.route("/collection", methods=["POST"])
def collection_add():
    return controllers.collection_add(request)


@collections.route("/collections")
def collections_get_all():
    return controllers.collections_get_all()


@collections.route("/collection/<collection_id>")
def collection_get_by_id(collection_id):
    return controllers.collection_get_by_id(collection_id)


@collections.route("/collection/<collection_id>", methods=["PUT"])
def collection_update_by_id(collection_id):
    return controllers.collection_update_by_id(request, collection_id)


@collections.route("/collection/delete/<collection_id>", methods=["DELETE"])
def collection_delete_by_id(collection_id):
    return controllers.collection_delete_by_id(collection_id)
