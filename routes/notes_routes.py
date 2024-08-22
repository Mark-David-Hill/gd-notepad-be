from flask import Blueprint, request

import controllers

notes = Blueprint("note", __name__)


@notes.route("/note", methods=["POST"])
def note_add():
    return controllers.note_add(request)


@notes.route("/notes")
def notes_get_all():
    return controllers.notes_get_all()


@notes.route("/note/<note_id>")
def note_get_by_id(note_id):
    return controllers.note_get_by_id(note_id)


@notes.route("/note/<note_id>", methods=["PUT"])
def note_update_by_id(note_id):
    return controllers.note_update_by_id(request, note_id)


@notes.route("/note/delete/<note_id>", methods=["DELETE"])
def note_delete_by_id(note_id):
    return controllers.note_delete_by_id(note_id)
