from flask import session, render_template, request, flash
from autogestion_alumnos.models import User
from autogestion_alumnos import app, db, bcrypt
from autogestion_alumnos.utils import go_to
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
def home():
    return go_to("log_in")


@app.route('/<default_page>')
def redirected_home(default_page):
    return go_to("log_in")


@app.route('/sign_up', methods=["POST", "GET"])
def sign_up():
    if current_user.is_authenticated:
        return go_to("log_in")
    if request.method == "POST":
        userName = request.form["userName"]
        password = request.form["password"]
        dni = request.form["dni"]
        if register_user(dni, userName, password):
            flash("Registered successfully. Please Log In.")
            return go_to("log_in")
        flash("That user is already registered. Please try with another user combination.")
        return render_template('signUp.html')
    return render_template('signUp.html')


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


@app.route('/logout', methods=["POST", "GET"])
def log_out():
    logout_user()
    return go_to("log_in")


@app.route('/login', methods=["POST", "GET"])
def log_in():
    if current_user.is_authenticated:
        return go_to("dashboard")
    if request.method == "POST":
        session.permanent = True
        user_name = request.form["userName"]
        password = request.form["password"]
        registered = is_user_registered(user_name, password)
        if registered:
            user = User.query.filter_by(name=user_name).first()
            login_user(user)
            return go_to("dashboard")
    return render_template('login.html')


def is_user_registered(user_name, password):
    temporal_user = User.query.filter_by(name=user_name).first()
    if temporal_user is None:
        flash("User not registered.")
        return False
    if bcrypt.check_password_hash(temporal_user.password, password):
        return True
    flash("Password incorrect. Please try again.")
    return False


@app.route('/recover_password')
def recover_password():
    if current_user.is_authenticated:
        return go_to("dashboard")
    return render_template('recover_password.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
