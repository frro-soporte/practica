from autogestion_alumnos import db


class Users(db.Model):
    id_user = db.Column('id_user', db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    dni = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
