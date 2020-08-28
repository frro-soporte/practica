from flask import Blueprint, render_template
from flask_backend.utils import go_to
from flask_login import login_required
# if we need to import app after we need to do 'from flask import current_app'

main = Blueprint('main', __name__)


@main.route("/")
def home():
    return go_to("users.log_in")


@main.route('/<default_page>')
def redirected_home(default_page):
    return go_to("users.log_in")


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
