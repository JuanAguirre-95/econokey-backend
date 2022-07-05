from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, current_user
from marshmallow import ValidationError

from app.models.wallet import WalletSchema
from app.services.vault.vault_controller import vault_controller

wallet_view = Blueprint("wallet_view", __name__, url_prefix="/wallets")


@wallet_view.get("/")
@jwt_required()
def list_wallets():
    vault_controller.load_vault(current_user)
    current_vault = vault_controller.open_vault
    wallets = current_vault.wallets
    return jsonify(wallets)


@wallet_view.get("/wallet")
@jwt_required()
def get_wallet():
    element_id = request.args.get("element_id")
    vault_controller.load_vault(current_user)
    current_vault = vault_controller.open_vault
    wallet = current_vault.get_note(element_id)
    if wallet:
        return jsonify(wallet)
    return {"error": f"Could not find note with id '{element_id}'"}, 404


@wallet_view.post("/wallet")
@jwt_required()
def add_wallet():
    vault_controller.load_vault(current_user)
    current_vault = vault_controller.open_vault

    payload = request.get_json()
    try:
        element = WalletSchema().load(payload["element"])
    except ValidationError as err:
        return err.normalized_messages()
    current_vault.add_wallet(element)
    vault_controller.save_vault(current_user)

    return element


@wallet_view.put("/wallet")
@jwt_required()
def update_wallet():
    vault_controller.load_vault(current_user)
    current_vault = vault_controller.open_vault

    payload = request.get_json()
    try:
        element = WalletSchema().load(payload["element"])
    except ValidationError as err:
        return err.normalized_messages()
    current_vault.update_wallet(payload["element_id"], element)
    vault_controller.save_vault(current_user)

    return element


@wallet_view.delete("/wallet")
@jwt_required()
def delete_wallet():
    element_id = request.get_json().get("element_id")
    vault_controller.load_vault(current_user)
    current_vault = vault_controller.open_vault
    wallet = current_vault.delete_wallet(element_id)
    if wallet:
        vault_controller.save_vault(current_user)
        return jsonify(wallet)
    return {"error": f"Could not find wallet with id '{element_id}'"}, 404
