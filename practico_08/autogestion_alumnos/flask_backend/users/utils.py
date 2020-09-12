from flask_backend.models import User, Subject
from flask_backend import db, bcrypt


def register_subject(subject_name, theory_hs, practice_hs, division, score, condition, theory_p, practice_p, username):
    user_id = User.query.filter_by(name=username).first().id
    try:
        registered_subject = Subject(name=subject_name, theory_ddhhhh=theory_hs, practice_ddhhhh=practice_hs, division=division, score=score, condition=condition, theory_professor=theory_p, practice_professor=practice_p, user_id=user_id)
        db.session.add(registered_subject)
        db.session.commit()
        return dict(status="ok", data=dict(registered_subject.serialize()))
    except:
        return dict(status="false")


def modify_subject(subject_id, subject_name, theory_hs, practice_hs, division, score, condition, theory_p, practice_p):
    subject = Subject.query.filter_by(id=subject_id).first()
    try:
        subject.name = subject_name
        subject.theory_ddhhhh = theory_hs
        subject.practice_ddhhhh = practice_hs
        subject.division = division
        subject.score = score
        subject.condition = condition
        subject.theory_professor = theory_p
        subject.practice_professor = practice_p
        db.session.commit()
        return True
    except:
        return False


def delete_subject(subject):
    try:
        db.session.delete(subject)
        db.session.commit()
        return True
    except:
        return False


def register_user(dni, user_name, password, legajo):
    if is_user_created(dni, user_name, legajo):
        return False
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    registered_user = User(dni=dni, name=user_name, password=hashed_password, legajo=legajo)
    db.session.add(registered_user)
    db.session.commit()
    return True


def is_user_created(dni=None, user_name=None, legajo=None):
    dni_registered = User.query.filter_by(dni=dni).first()
    user_registered = User.query.filter_by(name=user_name).first()
    legajo_registered = User.query.filter_by(legajo=legajo).first()
    if dni_registered is None and user_registered is None and legajo_registered is None:
        return False
    else:
        return True


def is_user_registered(user_name, password):
    temporal_user = User.query.filter_by(name=user_name).first()
    if temporal_user is None:
        return False
    if bcrypt.check_password_hash(temporal_user.password, password):
        return True
    return False
