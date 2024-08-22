from flask import jsonify
from uuid import UUID

from db import db
from models.release_profiles import ReleaseProfiles, release_profile_schema, release_profiles_schema
from util.reflection import populate_object
from lib.authenticate import auth


@auth
def profile_add(req):
    post_data = req.form if req.form else req.json

    if not post_data:
        return jsonify({"message": "all required fields must be submitted"}), 400
    
    new_profile = ReleaseProfiles.new_profile_obj()

    populate_object(new_profile, post_data)

    try:
        db.session.add(new_profile)
        db.session.commit()
        return jsonify({"message": "profile created", "result": release_profile_schema.dump(new_profile)}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not create profile"}), 400
    
    

@auth
def profiles_get_all():
    profiles_query = db.session.query(ReleaseProfiles).all()

    if not profiles_query:
        return jsonify({"message": "no profiles found"}), 404
    
    return jsonify({"message": "profiles found", "results": release_profiles_schema.dump(profiles_query)}), 200


@auth
def profile_get_by_id(profile_id):
    try:
        UUID(profile_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot get profile without a valid uuid"}), 400

    profile_query = db.session.query(ReleaseProfiles).filter(ReleaseProfiles.profile_id == profile_id).first()

    if not profile_query:
        return jsonify({"message": "profile does not exist"}), 404
    
    return jsonify({"message": "profile found", "result": release_profile_schema.dump(profile_query)}), 200


@auth
def profile_update_by_id(req, profile_id):
    post_data = req.form if req.form else req.json

    try:
        UUID(profile_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot update profile without a valid uuid"}), 400

    profile_query = db.session.query(ReleaseProfiles).filter(ReleaseProfiles.profile_id == profile_id).first()

    populate_object(profile_query, post_data)

    if not profile_query:
        return jsonify({"message": "profile does not exist"}), 404
    
    try:
        db.session.commit()
        return jsonify({"message": "profile updated", "result": release_profile_schema.dump(profile_query)}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not update profile"}), 400


@auth
def profile_delete_by_id(profile_id):
    try:
        UUID(profile_id, version=4)
    except Exception as e:
        return jsonify({"message": "cannot update profile without a valid uuid"}), 400

    profile_query = db.session.query(ReleaseProfiles).filter(ReleaseProfiles.profile_id == profile_id).first()

    if not profile_query:
        return jsonify({"message": "profile does not exist"}), 404
    
    try:
        db.session.delete(profile_query)
        db.session.commit()
        return jsonify({"message": "the profile was deleted"}), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"message": "could not delete profile"}), 400
        