import os
import uuid

from bcrypt import hashpw, gensalt
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, current_user

from app.models.password import PasswordSchema
from app.models.vault import Vault
from app.services.vault.vault_controller import vault_controller
from app.endpoints.vault.password import password_view
from app.endpoints.vault.note import note_view
from app.endpoints.vault.wallet import wallet_view

vault_view = Blueprint("vault_view", __name__, url_prefix="/vault")
vault_view.register_blueprint(password_view)
vault_view.register_blueprint(note_view)
vault_view.register_blueprint(wallet_view)


def validate_json_body(body: dict):
    pass


@vault_view.post("/")
def create_new_vault():
    """
    Creates a new vault, using the name and key provided by the user
    :return: JSON
    """
    payload = request.get_json()
    validate_json_body(payload)
    existing_vault = Vault.get_by_name(payload["vault_name"])
    if existing_vault:
        return {"error": "The vault name already exists"}, 400
    new_vault_data = Vault(vault_name=payload["vault_name"])
    new_vault_data.vault_id = str(uuid.uuid4())
    new_vault_data.vault_key = payload["vault_key"]
    new_vault_data.salt = os.urandom(16)
    new_vault_data.save()
    vault_controller.create_vault(new_vault_data)
    current_vault = vault_controller.get_vault().get_dict()
    return current_vault


@vault_view.get("/")
@jwt_required()
def get_current_vault():
    vault_controller.load_vault(current_user)
    return vault_controller.open_vault.get_dict()

