from flask import jsonify

from db import db
from models.release_profiles import ReleaseProfiles, release_profile_schema, release_profiles_schema
from util.reflection import populate_object
from util.controllers_util import *
from lib.authenticate import auth, validate_uuid4


@auth
def profile_add(req):
    return record_add(req, ReleaseProfiles.new_profile_obj(), release_profile_schema, "profile")
    

@auth
def profiles_get_all():
    return records_get_all(ReleaseProfiles, release_profiles_schema, "profiles")


@auth
def profile_get_by_id(profile_id):
    if not validate_uuid4(profile_id):
        return jsonify({"message": "cannot get profile without a valid uuid"}), 400

    profile_query = db.session.query(ReleaseProfiles).filter(ReleaseProfiles.profile_id == profile_id).first()
    return record_get_by_id(profile_query, release_profile_schema, "profile")


@auth
def profile_update_by_id(req, profile_id):
    if not validate_uuid4(profile_id):
        return jsonify({"message": "cannot update profile without a valid uuid"}), 400

    profile_query = db.session.query(ReleaseProfiles).filter(ReleaseProfiles.profile_id == profile_id).first()
    return record_update_by_id(req, profile_query, release_profile_schema, "profile")


@auth
def profile_delete_by_id(profile_id):
    if not validate_uuid4(profile_id):
        return jsonify({"message": "cannot update profile without a valid uuid"}), 400

    profile_query = db.session.query(ReleaseProfiles).filter(ReleaseProfiles.profile_id == profile_id).first()
    return record_delete_by_id(profile_query, "profile")
        