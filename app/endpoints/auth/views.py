"""Authentication module"""
import datetime

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from bcrypt import checkpw, hashpw, gensalt

from app.models.vault import Vault
from app.modules import db, jwt

login_view = Blueprint("login_view", __name__, url_prefix="/login")


# Register a callback function that takes whatever object is passed in as the
# identity when creating JWTs and converts it to a JSON serializable format.
@jwt.user_identity_loader
def user_identity_lookup(vault: Vault):
    return vault.id


# Register a callback function that loads a user from your database whenever
# a protected route is accessed. This should return any python object on a
# successful lookup, or None if the lookup failed for any reason (for example
# if the user has been deleted from the database).
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return Vault.query.filter_by(id=identity).one_or_none()


@login_view.post("/")
def login():
    """
    Obtain a JWT token that will be used to authenticate requests to the currently open vault.
    :return: JSON
    """
    vault_name = request.json.get("vault_name", None)
    vault_key = request.json.get("vault_key", None)

    vault = Vault.query.filter_by(vault_name=vault_name).one_or_none()
    if not vault or not vault.check_password(vault_key):
        return jsonify("Wrong username or password"), 401

    # Notice that we are passing in the actual sqlalchemy user object here
    access_token = create_access_token(identity=vault, expires_delta=datetime.timedelta(days=1))
    return jsonify(access_token=access_token)
