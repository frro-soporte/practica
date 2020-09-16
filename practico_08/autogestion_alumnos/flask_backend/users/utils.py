import datetime

from flask_backend.models import User, Subject, Task, Exam
from flask_backend import db, bcrypt


# SUBJECT METHODS


def is_subject_id_valid(subject_id):
    try:
        subject_id = Subject.query.filter_by(id=subject_id).first()
        if subject_id is None:
            return False
        return True
    except:
        return False


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


# TASK METHODS


def register_task(description, date, score, is_done, subject_id):
    if is_subject_id_valid(subject_id):
        try:
            if date == '':
                registered_task = Task(description=description, score=score, is_done=str(is_done),
                                       subject_id=subject_id)
            else:
                date_formatted = datetime.datetime.strftime(date, '%d/%m/%y')
                registered_task = Task(description=description, date=date_formatted, score=score, is_done=str(is_done), subject_id=subject_id)
            db.session.add(registered_task)
            db.session.commit()
            return dict(status="ok", data=dict(registered_task.serialize()))
        except:
            return dict(status="false", msg="task not saved")
    return dict(status="false", msg="subject id not valid")


def is_task_id_valid(task_id):
    try:
        task_id = Task.query.filter_by(id=task_id).first()
        if task_id is None:
            return False
        return True
    except:
        return False


def modify_task(task_id, description, date, score, is_done):
    task = Task.query.filter_by(id=task_id).first()
    try:
        if date == '':
            task.description = description
            task.date = None
            task.score = score
            task.is_done = str(is_done)
        else:
            if task.date != date:
                date_formatted = datetime.datetime.strftime(date, '%d/%m/%y')
                task.description = description
                task.date = date_formatted
                task.score = score
                task.is_done = str(is_done)
            else:
                task.description = description
                task.date = date
                task.score = score
                task.is_done = str(is_done)
        db.session.commit()
        return True
    except:
        return False


def delete_task(task):
    try:
        db.session.delete(task)
        db.session.commit()
        return True
    except:
        return False


# EXAM METHODS


def register_exam(description, date, score, subject_id):
    if is_subject_id_valid(subject_id):
        try:
            if date == '':
                registered_exam = Exam(description=description, score=score, subject_id=subject_id)
            else:
                date_formatted = datetime.datetime.strftime(date, '%d/%m/%y')
                registered_exam = Exam(description=description, date=date_formatted, score=score, subject_id=subject_id)
            db.session.add(registered_exam)
            db.session.commit()
            return dict(status="ok", data=dict(registered_exam.serialize()))
        except:
            return dict(status="false", msg="exam not saved")
    return dict(status="false", msg="subject id not valid")


def is_exam_id_valid(exam_id):
    try:
        exam_id = Exam.query.filter_by(id=exam_id).first()
        if exam_id is None:
            return False
        return True
    except:
        return False


def modify_exam(exam_id, description, date, score):
    exam = Exam.query.filter_by(id=exam_id).first()
    try:
        if date == '':
            exam.description = description
            exam.date = None
            exam.score = score
        else:
            if exam.date != date:
                date_formatted = datetime.datetime.strftime(date, '%d/%m/%y')
                exam.description = description
                exam.date = date_formatted
                exam.score = score
            else:
                exam.description = description
                exam.date = date
                exam.score = score
        db.session.commit()
        return True
    except:
        return False


def delete_exam(exam):
    try:
        db.session.delete(exam)
        db.session.commit()
        return True
    except:
        return False


# USER METHODS


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
