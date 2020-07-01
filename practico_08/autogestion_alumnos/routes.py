from flask import session, render_template, request, flash
from autogestion_alumnos.model import Users
from autogestion_alumnos import app, db
from autogestion_alumnos.utils import go_to, logged, delete_session_information


@app.route("/")
def home():
    return go_to("log_in")


@app.route('/<default_page>')
def redirected_home(default_page):
    return go_to("log_in")


@app.route('/sign_up', methods=["POST", "GET"])
def sign_up():
    if logged():
        return go_to("log_in")
    delete_session_information()
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
    registered_user = Users(dni=dni, name=user_name, password=password)
    db.session.add(registered_user)
    db.session.commit()
    return True


def is_user_created(dni=None, user_name=None):
    dni_registered = Users.query.filter_by(dni=dni).first()
    user_registered = Users.query.filter_by(name=user_name).first()
    if dni_registered is None and user_registered is None:
        return False
    else:
        return True


@app.route('/logout', methods=["POST", "GET"])
def log_out():
    delete_session_information()
    return go_to("log_in")


@app.route('/login', methods=["POST", "GET"])
def log_in():
    if logged():
        return go_to("dashboard")
    if request.method == "POST":
        session.permanent = True
        userName = request.form["userName"]
        password = request.form["password"]
        session["userName"] = userName
        session["password"] = password
        registered = is_user_registered()
        if registered:
            if logged():
                return go_to("dashboard")
        delete_session_information()
    return render_template('login.html')


def is_user_registered():
    temporal_user = Users.query.filter_by(name=session["userName"]).first()
    if temporal_user is None:
        flash("User not registered.")
        return False
    if temporal_user.password == session["password"]:
        return True
    flash("Password incorrect. Please try again.")
    return False


@app.route('/recover_password')
def recover_password():
    if logged():
        return go_to("dashboard")
    return render_template('recover_password.html')


@app.route('/dashboard')
def dashboard():
    if logged():
        return render_template('dashboard.html')
    return go_to("log_in")
