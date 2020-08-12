from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.log_in'


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    db.app = app
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from autogestion_alumnos.users.routes import users
    from autogestion_alumnos.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(main)

    return app
