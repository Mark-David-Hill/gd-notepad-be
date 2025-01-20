from flask import Blueprint, request

import controllers

relationships = Blueprint("relationship", __name__)


@relationships.route("/relationship", methods=["POST"])
def relationship_add():
    return controllers.relationship_add(request)


@relationships.route("/relationships")
def relationships_get_all():
    return controllers.relationships_get_all()


@relationships.route("/relationships/collection/<collection_id>")
def relationships_get_by_collection(collection_id):
    return controllers.relationships_get_by_collection(collection_id)


@relationships.route("/relationship/<relationship_id>")
def relationship_get_by_id(relationship_id):
    return controllers.relationship_get_by_id(relationship_id)


@relationships.route("/relationship/<relationship_id>", methods=["PUT"])
def relationship_update_by_id(relationship_id):
    return controllers.relationship_update_by_id(request, relationship_id)


@relationships.route("/relationship/delete/<relationship_id>", methods=["DELETE"])
def relationship_delete_by_id(relationship_id):
    return controllers.relationship_delete_by_id(relationship_id)
