from marshmallow.exceptions import ValidationError
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, current_user

from app.models.password import PasswordSchema
from app.services.vault.vault_controller import vault_controller

password_view = Blueprint("password_view", __name__, url_prefix="/passwords")


@password_view.get("/")
@jwt_required()
def list_passwords():
    vault_controller.load_vault(current_user)
    current_vault = vault_controller.open_vault
    passwords = current_vault.passwords
    return jsonify(passwords)


@password_view.get("/password")
@jwt_required()
def get_password():
    element_id = request.args.get("element_id")
    vault_controller.load_vault(current_user)
    current_vault = vault_controller.open_vault
    password = current_vault.get_wallet(element_id)
    if password:
        return jsonify(password)
    return {"error": f"Could not find password with id '{element_id}'"}, 404


@password_view.post("/password")
@jwt_required()
def add_password():
    vault_controller.load_vault(current_user)
    current_vault = vault_controller.open_vault

    payload = request.get_json()
    try:
        element = PasswordSchema().load(payload["element"])
    except ValidationError as err:
        return err.normalized_messages()
    current_vault.add_password(element)
    vault_controller.save_vault(current_user)

    return element


@password_view.put("/password")
@jwt_required()
def update_password():
    vault_controller.load_vault(current_user)
    current_vault = vault_controller.open_vault

    payload = request.get_json()
    try:
        element = PasswordSchema().load(payload["element"])
    except ValidationError as err:
        return err.normalized_messages()
    current_vault.update_password(payload["element_id"], element)
    vault_controller.save_vault(current_user)

    return element


@password_view.delete("/password")
@jwt_required()
def delete_password():
    element_id = request.get_json().get("element_id")
    vault_controller.load_vault(current_user)
    current_vault = vault_controller.open_vault
    password = current_vault.delete_password(element_id)
    if password:
        vault_controller.save_vault(current_user)
        return jsonify(password)
    return {"error": f"Could not find password with id '{element_id}'"}, 404
