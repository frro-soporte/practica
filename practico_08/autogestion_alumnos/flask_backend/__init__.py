from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
#from flask_bootstrap import Bootstrap


db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #bootstrap = Bootstrap(app)
    db.init_app(app)
    db.app = app
    bcrypt.init_app(app)
    jwt.init_app(app)

    from flask_backend.users.routes import users
    from flask_backend.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(main)

    return app
