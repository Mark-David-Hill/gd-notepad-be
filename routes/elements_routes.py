from flask import Blueprint, request

import controllers

elements = Blueprint("element", __name__)


@elements.route("/element", methods=["POST"])
def element_add():
    return controllers.element_add(request)


@elements.route("/element/tag", methods=["POST"])
def element_tag_update():
    return controllers.element_tag_update(request)


@elements.route("/elements")
def elements_get_all():
    return controllers.elements_get_all()


@elements.route("/elements/tag/<tag_id>")
def elements_get_all_with_tag(tag_id):
    return controllers.elements_get_all_with_tag(tag_id)


@elements.route("/element/<element_id>")
def element_get_by_id(element_id):
    return controllers.element_get_by_id(element_id)


@elements.route("/element/<element_id>", methods=["PUT"])
def element_update_by_id(element_id):
    return controllers.element_update_by_id(request, element_id)


@elements.route("/element/delete/<element_id>", methods=["DELETE"])
def element_delete_by_id(element_id):
    return controllers.element_delete_by_id(element_id)
