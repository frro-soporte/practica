from flask import Flask, session, redirect, render_template, url_for, request, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "frro_soporte"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=3)

db = SQLAlchemy(app)


class UserModel(db.Model):
    id = db.Column('id_user', db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    dni = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route("/")
def home():
    return go_to("log_in")


@app.route('/<default_page>')
def redirected_home(default_page):
    return go_to("log_in")


@app.route('/dashboard')
def dashboard():
    if logged():
        return render_template('dashboard.html')
    return go_to("log_in")


@app.route('/sign_up', methods=["POST", "GET"])
def sign_up():
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
    registered_user = UserModel(dni=dni, name=user_name, password=password)
    db.session.add(registered_user)
    db.session.commit()
    return True


def is_user_created(dni=None, user_name=None):
    dni_registered = UserModel.query.filter_by(dni=dni).first()
    user_registered = UserModel.query.filter_by(name=user_name).first()
    if dni_registered is None and user_registered is None:
        return False
    else:
        return True


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
            return go_to("dashboard")
        delete_session_information()
    return render_template('login.html')


def is_user_registered():
    temporal_user = UserModel.query.filter_by(name=session["userName"]).first()
    if temporal_user is None:
        flash("User not registered.")
        return False
    print(temporal_user.password)
    print(session["password"])
    if temporal_user.password == session["password"]:
        return True
    flash("Password incorrect. Please try again.")
    return False


@app.route('/recover_password')
def recover_password():
    if logged():
        return go_to("dashboard")
    return render_template('recover_password.html')


@app.route('/logout', methods=["POST", "GET"])
def log_out():
    delete_session_information()
    return go_to("log_in")


def logged():
    if "userName" in session and "password" in session:
        return True
    return False


def delete_session_information():
    if logged():
        session.pop("userName", None)
        session.pop("password", None)
        session.pop("dni", None)
    return True


def go_to(page: str):
    return redirect(url_for(page))


if __name__ == '__main__':
    db.create_all()
    app.run(port=3000, debug=True)
