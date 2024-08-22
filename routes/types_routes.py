from flask import Blueprint, request

import controllers

types = Blueprint("type", __name__)


@types.route("/type", methods=["POST"])
def type_add():
    return controllers.type_add(request)


@types.route("/types")
def types_get_all():
    return controllers.types_get_all()


@types.route("/type/<type_id>")
def type_get_by_id(type_id):
    return controllers.type_get_by_id(type_id)


@types.route("/type/<type_id>", methods=["PUT"])
def type_update_by_id(type_id):
    return controllers.type_update_by_id(request, type_id)


@types.route("/type/delete/<type_id>", methods=["DELETE"])
def type_delete_by_id(type_id):
    return controllers.type_delete_by_id(type_id)
