from flask import Blueprint, request

import controllers

profiles = Blueprint("profile", __name__)


@profiles.route("/profile", methods=["POST"])
def profile_add():
    return controllers.profile_add(request)


@profiles.route("/profiles")
def profiles_get_all():
    return controllers.profiles_get_all()


@profiles.route("/profile/<profile_id>")
def profile_get_by_id(profile_id):
    return controllers.profile_get_by_id(profile_id)


@profiles.route("/profile/<profile_id>", methods=["PUT"])
def profile_update_by_id(profile_id):
    return controllers.profile_update_by_id(request, profile_id)


@profiles.route("/profile/<profile_id>", methods=["DELETE"])
def profile_delete_by_id(profile_id):
    return controllers.profile_delete_by_id(profile_id)
