from flask import Blueprint, render_template
from flask_backend.utils import go_to
from flask_login import login_required
# if we need to import app after we need to do 'from flask import current_app'

main = Blueprint('main', __name__)

