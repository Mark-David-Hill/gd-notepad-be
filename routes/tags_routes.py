from flask import Blueprint, request

import controllers

tags = Blueprint("tag", __name__)


@tags.route("/tag", methods=["POST"])
def tag_add():
    return controllers.tag_add(request)


@tags.route("/tags")
def tags_get_all():
    return controllers.tags_get_all()


@tags.route("/tag/<tag_id>")
def tag_get_by_id(tag_id):
    return controllers.tag_get_by_id(tag_id)


@tags.route("/tag/<tag_id>", methods=["PUT"])
def tag_update_by_id(tag_id):
    return controllers.tag_update_by_id(request, tag_id)


@tags.route("/tag/<tag_id>", methods=["DELETE"])
def tag_delete_by_id(tag_id):
    return controllers.tag_delete_by_id(tag_id)
