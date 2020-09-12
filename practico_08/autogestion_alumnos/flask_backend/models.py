from flask_backend import db
from flask_login import UserMixin

from sqlalchemy.inspection import inspect


class Serializer(object):
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


class User(db.Model, UserMixin):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    dni = db.Column(db.Integer, unique=True, nullable=False)
    legajo = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

    # son
    subjects = db.relationship('Subject', backref='user', lazy=True)

    def __repr__(self):
        return f"User('dni: {self.dni}', 'name: {self.name}', 'legajo: {self.legajo}')"

    def serialize(self):
        d = Serializer.serialize(self)
        return d

    def serialize_list(self, elements):
        d = Serializer.serialize_list(elements)
        return d


class Subject(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    theory_ddhhhh = db.Column(db.String(6), nullable=True)
    practice_ddhhhh = db.Column(db.String(6), nullable=True)
    division = db.Column(db.String(3), nullable=False)
    score = db.Column(db.String(2), nullable=True)
    condition = db.Column(db.String(10), nullable=False)
    theory_professor = db.Column(db.String(250), nullable=True)
    practice_professor = db.Column(db.String(250), nullable=True)

    # parent
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # children
    exams = db.relationship('Exam', backref='subject', lazy=True)
    tasks = db.relationship('Task', backref='subject', lazy=True)

    def __repr__(self):
        return f"Subject('{self.name}', '{self.division}', '{self.score}', '{self.condition}'," \
               f"'{self.practice_ddhhhh}', '{self.theory_ddhhhh}', '{self.theory_professor}', '{self.practice_professor}')"

    def serialize(self):
        d = Serializer.serialize(self)
        del d['user']
        return d

    @staticmethod
    def serialize_list(elements):
        d = Serializer.serialize_list(elements)
        return d


class Exam(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    score = db.Column(db.String(2), nullable=True)

    # parent
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)

    def __repr__(self):
        return f"Exam('{self.description}', '{self.date}', '{self.score}')"

    def serialize(self):
        d = Serializer.serialize(self)
        del d['subject']
        return d

    def serialize_list(self, elements):
        d = Serializer.serialize_list(elements)
        return d


class Task(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    date = db.Column(db.DateTime, nullable=True)
    score = db.Column(db.String(2), nullable=True)
    is_done = db.Column(db.Boolean, nullable=False, default=False)

    # parent
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)

    def __repr__(self):
        return f"Task('{self.description}', '{self.date}', '{self.score}', '{self.is_done}')"

    def serialize(self):
        d = Serializer.serialize(self)
        del d['subject']
        return d

    def serialize_list(self, elements):
        d = Serializer.serialize_list(elements)
        return d
