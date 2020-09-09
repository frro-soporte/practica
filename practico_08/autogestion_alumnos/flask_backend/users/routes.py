from datetime import timedelta

from flask import Blueprint, request, session, jsonify
from flask_backend import jwt
from flask_backend.models import User
from flask_backend.users.utils import register_user, is_user_registered
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt, get_jwt_identity

users = Blueprint('users', __name__)


@users.route('/logout', methods=["DELETE"])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return dict(status="ok")


blacklist = set()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


@users.route('/sign_up', methods=["POST"])
def sign_up():
    if request.method == "POST":
        userName = request.json.get("userName", None)
        password = request.json.get("password", None)
        legajo = request.json.get("legajo", None)
        dni = request.json.get("dni", None)
        if not userName:
            return dict(status="error", msg="Missing userName")
        if not password:
            return dict(status="error", msg="Missing password")
        if not legajo:
            return dict(status="error", msg="Missing legajo")
        if not dni:
            return dict(status="error", msg="Missing dni")
        if register_user(dni, userName, password, legajo):
            return dict(status="ok")
        return dict(status="error", msg="Already registered")
    return dict(status="error", msg="Request not allowed")


@users.route('/login', methods=["POST", "GET"])
def log_in():
    if request.method == "POST":
        session.permanent = True
        user_name = request.json.get("userName", None)
        password = request.json.get("password", None)
        if not user_name:
            return dict(status="error", msg="Missing user_name")
        if not password:
            return dict(status="error", msg="Missing password")
        registered = is_user_registered(user_name, password)
        if registered:
            user = User.query.filter_by(name=user_name).first()
            expires = timedelta(days=365)
            access_token = create_access_token(identity=user.name, expires_delta=expires)
            return dict(status="ok", data=dict(access_token=access_token))
        return dict(status="error", msg="Bad user name or password")
    return dict(status="error", msg="Request not allowed")


@users.route('/test_token', methods=["GET"])
@jwt_required
def recover_password():
    if request.method == "GET":
        current_user = get_jwt_identity()
        return dict(status="ok", data=dict(logged_in_as=current_user))
    return dict(status="error", msg="Request not allowed")

