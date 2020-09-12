from datetime import timedelta

from flask import Blueprint, request, session
from flask_backend import jwt
from flask_backend.models import User, Subject
from flask_backend.users.utils import register_user, is_user_registered, register_subject, delete_subject, \
    modify_subject
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


@users.route('/subject', methods=["POST", "DELETE", "GET", "PUT"])
@jwt_required
def subject():
    if request.method == "POST":
        current_user = get_jwt_identity()
        name = request.json.get("name", None)
        theory_ddhhhh = request.json.get("theoryddhhhh", None)
        practice_ddhhhh = request.json.get("practiceddhhhh", None)
        division = request.json.get("division", None)
        score = request.json.get("score", None)
        condition = request.json.get("condition", None)
        theory_professor = request.json.get("theory_professor", None)
        practice_professor = request.json.get("practice_professor", None)

        registered_subject = register_subject(
            name,
            theory_ddhhhh,
            practice_ddhhhh,
            division,
            score,
            condition,
            theory_professor,
            practice_professor,
            current_user
        )
        if registered_subject['status'] == "ok":
            return dict(status="ok", subject=registered_subject['data'])
        return dict(status="error", msg="subject not saved")

    if request.method == "GET":
        subject_id = request.json.get("id", None)
        subject = Subject.query.filter_by(id=subject_id).first()
        if subject is None:
            return dict(status="error", msg="Subject not found")
        return dict(status="ok", data=dict(subject=subject.serialize()))

    if request.method == "DELETE":
        subject_id = request.json.get("id", None)
        subject = Subject.query.filter_by(id=subject_id).first()
        if delete_subject(subject):
            return dict(status="ok")
        return dict(status="error", msg="subject not deleted")

    if request.method == "PUT":
        subject_id = request.json.get("id", None)
        name = request.json.get("name", None)
        theory_ddhhhh = request.json.get("theoryddhhhh", None)
        practice_ddhhhh = request.json.get("practiceddhhhh", None)
        division = request.json.get("division", None)
        score = request.json.get("score", None)
        condition = request.json.get("condition", None)
        theory_professor = request.json.get("theory_professor", None)
        practice_professor = request.json.get("practice_professor", None)

        if modify_subject(
            subject_id,
            name,
            theory_ddhhhh,
            practice_ddhhhh,
            division,
            score,
            condition,
            theory_professor,
            practice_professor,
        ):
            return dict(status="ok")
        return dict(status="error", msg="subject not updated")

    return dict(status="error", msg="request not allowed")


@users.route('/subjects', methods=["GET"])
@jwt_required
def get_subjects():
    if request.method == "GET":
        current_user = get_jwt_identity()
        user_id = User.query.filter_by(name=current_user).first().id
        subjects = Subject.query.filter_by(user_id=user_id).all()
        return dict(status="ok", data=dict(subjects=Subject.serialize_list(elements=subjects)))
    return dict(status="error", msg="Request not allowed")

