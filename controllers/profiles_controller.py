from flask import jsonify

from db import db
from models.release_profiles import ReleaseProfiles, release_profile_schema, release_profiles_schema
from models.games import Games
from util.controllers_util import *
from lib.authenticate import auth, validate_uuid4


@auth
def profile_add(req):
    post_data = req.form if req.form else req.json
    if not validate_uuid4(post_data.get("game_id")):
        return jsonify({"message": "could not create profile, must provide a valid uuid for game id"}), 400
    
    game_query = db.session.query(Games).filter(Games.game_id == post_data.get("game_id")).first()
    
    if  not game_query:
        return jsonify({"message": "could not create profile, game does not exist"})
    
    existing_profiles = db.session.query(ReleaseProfiles).filter(ReleaseProfiles.game_id == post_data.get("game_id")).all()

    if existing_profiles:
        return jsonify({"message": "could not create profile, that game already has a profile"})
    
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
        