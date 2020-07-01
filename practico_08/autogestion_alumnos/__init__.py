from flask import Flask
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "frro_soporte"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=3)

db = SQLAlchemy(app)

from autogestion_alumnos import routes
