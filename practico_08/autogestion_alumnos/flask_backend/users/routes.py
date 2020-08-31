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
    return jsonify({"status": "ok", "msg": "Successfully logged out"}), 200


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
            return jsonify({"status": "error", "msg": "Missing userName"}), 400
        if not password:
            return jsonify({"status": "error", "msg": "Missing password"}), 400
        if not legajo:
            return jsonify({"status": "error", "msg": "Missing legajo"}), 400
        if not dni:
            return jsonify({"status": "error", "msg": "Missing dni"}), 400
        if register_user(dni, userName, password, legajo):
            return jsonify({"status": "ok"}), 200
        return jsonify({"status": "error", "msg": "Already registered"}), 400
    return jsonify({"status": "error", "msg": "Request not allowed"}), 400


@users.route('/login', methods=["POST", "GET"])
def log_in():
    if request.method == "POST":
        session.permanent = True
        user_name = request.json.get("userName", None)
        password = request.json.get("password", None)
        if not user_name:
            return jsonify({"status": "error", "msg": "Missing user_name"}), 400
        if not password:
            return jsonify({"status": "error", "msg": "Missing password"}), 400
        registered = is_user_registered(user_name, password)
        if registered:
            user = User.query.filter_by(name=user_name).first()
            access_token = create_access_token(identity=user.name)
            return jsonify({"status": "ok", "msg": {"access_token": access_token}}), 200
        return jsonify({"status": "error", "msg": "Bad user name or password"}), 401
    return jsonify({"status": "error", "msg": "Request not allowed"}), 400


@users.route('/test_token', methods=["GET"])
@jwt_required
def recover_password():
    if request.method == "GET":
        current_user = get_jwt_identity()
        return jsonify({"status": "ok", "msg": {"logged_in_as": current_user}}), 200
    return jsonify({"status": "error", "msg": "Request not allowed"}), 400
