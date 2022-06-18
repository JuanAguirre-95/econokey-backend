from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, current_user
from marshmallow import ValidationError

from app.models.note import NoteSchema
from app.services.vault.vault_controller import vault_controller

note_view = Blueprint("note_view", __name__, url_prefix="/notes")

@note_view.get("/")
@jwt_required()
def list_notes():
    vault_controller.load_vault(current_user)
    current_vault = vault_controller.open_vault
    notes = current_vault.notes
    return jsonify(notes)


@note_view.get("/note")
@jwt_required()
def get_note():
    element_id = request.args.get("element_id")
    vault_controller.load_vault(current_user)
    current_vault = vault_controller.open_vault
    note = current_vault.get_note(element_id)
    if note:
        return jsonify(note)
    return {"error": f"Could not find note with id '{element_id}'"}, 404


@note_view.post("/note")
@jwt_required()
def add_note():
    vault_controller.load_vault(current_user)
    current_vault = vault_controller.open_vault

    payload = request.get_json()
    try:
        element = NoteSchema().load(payload["element"])
    except ValidationError as err:
        return err.normalized_messages()
    current_vault.add_note(element)
    vault_controller.save_vault(current_user)

    return element


@note_view.put("/note")
@jwt_required()
def update_note():
    vault_controller.load_vault(current_user)
    current_vault = vault_controller.open_vault

    payload = request.get_json()
    try:
        element = NoteSchema().load(payload["element"])
    except ValidationError as err:
        return err.normalized_messages()
    current_vault.update_note(payload["element_id"], element)
    vault_controller.save_vault(current_user)

    return element


@note_view.delete("/note")
@jwt_required()
def delete_note():
    element_id = request.get_json().get("element_id")
    vault_controller.load_vault(current_user)
    current_vault = vault_controller.open_vault
    note = current_vault.delete_note(element_id)
    if note:
        vault_controller.save_vault(current_user)
        return jsonify(note)
    return {"error": f"Could not find note with id '{element_id}'"}, 404
