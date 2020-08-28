from flask import Blueprint, render_template, request, flash, session
from flask_backend.models import User
from flask_backend.utils import go_to
from flask_backend.users.utils import register_user, is_user_registered
from flask_login import login_user, current_user, logout_user

users = Blueprint('users', __name__)


@users.route('/sign_up', methods=["POST", "GET"])
def sign_up():
    if current_user.is_authenticated:
        return go_to("users.log_in")
    if request.method == "POST":
        userName = request.form["userName"]
        password = request.form["password"]
        dni = request.form["dni"]
        if register_user(dni, userName, password):
            flash("Registered successfully. Please Log In.")
            return go_to("users.log_in")
        flash("That user is already registered. Please try with another user combination.")
        return render_template('signUp.html')
    return render_template('signUp.html')


@users.route('/logout', methods=["POST", "GET"])
def log_out():
    logout_user()
    return go_to("users.log_in")


@users.route('/login', methods=["POST", "GET"])
def log_in():
    if current_user.is_authenticated:
        return go_to("main.dashboard")
    if request.method == "POST":
        session.permanent = True
        user_name = request.form["userName"]
        password = request.form["password"]
        registered = is_user_registered(user_name, password)
        if registered:
            user = User.query.filter_by(name=user_name).first()
            login_user(user)
            return go_to("main.dashboard")
    return render_template('login.html')


@users.route('/recover_password')
def recover_password():
    if current_user.is_authenticated:
        return go_to("main.dashboard")
    return render_template('recover_password.html')
