from autogestion_alumnos import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    dni = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    subjects = db.relationship('Subject', backref='author', lazy=True)

    def __repr__(self):
        return f"User('dni: {self.dni}', 'name: {self.name}')"


class Subject(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    theory_professor = db.Column(db.String(250), nullable=False)
    practice_professor = db.Column(db.String(250), nullable=False)
    theory_ddhhhh = db.Column(db.String(6), nullable=True)
    practice_ddhhhh = db.Column(db.String(6), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Subject('{self.name}', '{self.theory_professor}', '{self.theory_ddhhhh}', '{self.practice_professor}'," \
               f"'{self.practice_ddhhhh}')"
