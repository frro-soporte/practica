from flask_backend import db
from flask_login import UserMixin


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


subjects_professors_association_table = db.Table('subjects_professors_association_table', db.metadata,
                                                 db.Column('subject_id', db.Integer, db.ForeignKey('subject.id')),
                                                 db.Column('professor_id', db.Integer, db.ForeignKey('professor.id')),
                                                 )


class Subject(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    theory_ddhhhh = db.Column(db.String(6), nullable=True)
    practice_ddhhhh = db.Column(db.String(6), nullable=True)
    division = db.Column(db.String(3), nullable=False)
    score = db.Column(db.String(2), nullable=True)
    condition = db.Column(db.String(10), nullable=False)

    # parent
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # children
    exams = db.relationship('Exam', backref='subject', lazy=True)
    tasks = db.relationship('Task', backref='subject', lazy=True)

    # association to professors
    professors = db.relationship('Professor', secondary=subjects_professors_association_table, back_populates='subjects',
                                 lazy=True)

    def __repr__(self):
        return f"Subject('{self.name}', '{self.division}', '{self.score}', '{self.condition}'," \
               f"'{self.practice_ddhhhh}', '{self.theory_ddhhhh}')"


class Professor(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=True)
    questions_hour = db.Column(db.String(250), nullable=True)
    type_of_class = db.Column(db.String(10), nullable=True)

    # association to subjects
    subjects = db.relationship('Subject', secondary=subjects_professors_association_table, back_populates='professors',
                               lazy=True)

    def __repr__(self):
        return f"Professor('{self.name}', '{self.email}', '{self.questions_hour}', '{self.type_of_class}')"


class Exam(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    score = db.Column(db.String(2), nullable=True)

    # parent
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)

    def __repr__(self):
        return f"Exam('{self.description}', '{self.date}', '{self.score}')"


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
