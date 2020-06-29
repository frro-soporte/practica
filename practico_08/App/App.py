from flask import Flask, session, redirect, render_template, url_for, request
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "frro_soporte"
app.permanent_session_lifetime = timedelta(minutes=3)


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


@app.route('/sign_up', methods=["POST"])
def sign_up():
    delete_session_information()
    if request.method == "POST":
        return go_to("log_in")
    return render_template('signUp.html')


@app.route('/login', methods=["POST"])
def log_in():
    if logged():
        return go_to("dashboard")
    if request.method == "POST":
        session.permanent = True
        userName = request.form["userName"]
        password = request.form["password"]
        session["userName"] = userName
        session["password"] = password
        return go_to("dashboard")
    return render_template('login.html')


@app.route('/logout')
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
    return True


def go_to(page: str):
    return redirect(url_for(page))


if __name__ == '__main__':
    app.run(port=3000, debug=True)
