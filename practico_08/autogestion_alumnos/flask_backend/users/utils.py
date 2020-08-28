from flask import flash
from flask_backend.models import User
from flask_backend import db, bcrypt


def register_user(dni, user_name, password):
    if is_user_created(dni, user_name):
        return False
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    registered_user = User(dni=dni, name=user_name, password=hashed_password)
    db.session.add(registered_user)
    db.session.commit()
    return True


def is_user_created(dni=None, user_name=None):
    dni_registered = User.query.filter_by(dni=dni).first()
    user_registered = User.query.filter_by(name=user_name).first()
    if dni_registered is None and user_registered is None:
        return False
    else:
        return True


def is_user_registered(user_name, password):
    temporal_user = User.query.filter_by(name=user_name).first()
    if temporal_user is None:
        flash("User not registered.")
        return False
    if bcrypt.check_password_hash(temporal_user.password, password):
        return True
    flash("Password incorrect. Please try again.")
    return False
