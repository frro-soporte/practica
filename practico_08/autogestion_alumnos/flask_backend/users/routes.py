from datetime import timedelta

from flask import Blueprint, request, session
from flask_backend import jwt
from flask_backend.models import User, Subject, Task, Exam
from flask_backend.users.utils import register_user, is_user_registered, register_subject, delete_subject, \
    modify_subject, register_task, delete_task, is_subject_id_valid, is_task_id_valid, modify_task, register_exam, \
    delete_exam, is_exam_id_valid, modify_exam
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt, get_jwt_identity

users = Blueprint('users', __name__)


@users.route('/logout', methods=["DELETE"])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return dict(status="ok")


blacklist = set()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist


# USER METHODS


@users.route('/sign_up', methods=["POST"])
def sign_up():
    if request.method == "POST":
        userName = request.json.get("userName", None)
        password = request.json.get("password", None)
        legajo = request.json.get("legajo", None)
        dni = request.json.get("dni", None)
        if not userName:
            return dict(status="error", msg="Missing userName")
        if not password:
            return dict(status="error", msg="Missing password")
        if not legajo:
            return dict(status="error", msg="Missing legajo")
        if not dni:
            return dict(status="error", msg="Missing dni")
        if register_user(dni, userName, password, legajo):
            return dict(status="ok")
        return dict(status="error", msg="Already registered")
    return dict(status="error", msg="Request not allowed")


@users.route('/login', methods=["POST", "GET"])
def log_in():
    if request.method == "POST":
        session.permanent = True
        user_name = request.json.get("userName", None)
        password = request.json.get("password", None)
        if not user_name:
            return dict(status="error", msg="Missing user_name")
        if not password:
            return dict(status="error", msg="Missing password")
        registered = is_user_registered(user_name, password)
        if registered:
            user = User.query.filter_by(name=user_name).first()
            expires = timedelta(days=365)
            access_token = create_access_token(identity=user.name, expires_delta=expires)
            return dict(status="ok", data=dict(access_token=access_token))
        return dict(status="error", msg="Bad user name or password")
    return dict(status="error", msg="Request not allowed")


# SUBJECT METHODS


@users.route('/subject', methods=["POST", "DELETE", "PUT"])
@jwt_required
def subject():
    if request.method == "POST":
        current_user = get_jwt_identity()
        name = request.json.get("name", None)
        theory_ddhhhh = request.json.get("theoryddhhhh", None)
        practice_ddhhhh = request.json.get("practiceddhhhh", None)
        division = request.json.get("division", None)
        score = request.json.get("score", None)
        condition = request.json.get("condition", None)
        theory_professor = request.json.get("theory_professor", None)
        practice_professor = request.json.get("practice_professor", None)

        registered_subject = register_subject(
            name,
            theory_ddhhhh,
            practice_ddhhhh,
            division,
            score,
            condition,
            theory_professor,
            practice_professor,
            current_user
        )
        if registered_subject['status'] == "ok":
            return dict(status="ok", subject=registered_subject['data'])
        return dict(status="error", msg="subject not saved")

    if request.method == "DELETE":
        subject_id = request.json.get("id", None)
        subject = Subject.query.filter_by(id=subject_id).first()
        if subject is not None:
            if delete_subject(subject):
                return dict(status="ok")
            return dict(status="error", msg="subject not deleted")
        return dict(status="error", msg="subject not found")

    if request.method == "PUT":
        subject_id = request.json.get("id", None)
        name = request.json.get("name", None)
        theory_ddhhhh = request.json.get("theoryddhhhh", None)
        practice_ddhhhh = request.json.get("practiceddhhhh", None)
        division = request.json.get("division", None)
        score = request.json.get("score", None)
        condition = request.json.get("condition", None)
        theory_professor = request.json.get("theory_professor", None)
        practice_professor = request.json.get("practice_professor", None)

        if is_subject_id_valid(subject_id):
            if modify_subject(
                subject_id,
                name,
                theory_ddhhhh,
                practice_ddhhhh,
                division,
                score,
                condition,
                theory_professor,
                practice_professor,
            ):
                return dict(status="ok")
            return dict(status="error", msg="subject not updated")
        return dict(status="error", msg="subject not found")
    return dict(status="error", msg="request not allowed")


@users.route('/getsubject', methods=["POST"])
@jwt_required
def get_subject():
    if request.method == "POST":
        subject_id = request.json.get("id", None)
        subject = Subject.query.filter_by(id=subject_id).first()
        if subject is None:
            return dict(status="error", msg="Subject not found")
        return dict(status="ok", data=dict(subject={
            'id': subject.id,
            'name': subject.name,
            'division': subject.division,
            'score': subject.score,
            'condition': subject.condition,
            'theory_ddhhhh': subject.theory_ddhhhh,
            'theory_professor': subject.theory_professor,
            'practice_ddhhhh': subject.practice_ddhhhh,
            'practice_professor': subject.practice_professor,
            'exams': subject.serialize_list(subject.exams),
            'tasks': subject.serialize_list(subject.tasks),
        }))
    return dict(status="error", msg="Request not allowed")


@users.route('/subjects', methods=["GET"])
@jwt_required
def get_subjects():
    if request.method == "GET":
        current_user = get_jwt_identity()
        user_id = User.query.filter_by(name=current_user).first().id
        subjects = Subject.query.filter_by(user_id=user_id).all()
        final_subjects = []
        for subject in subjects:
            final_subjects.append({
            'id': subject.id,
            'name': subject.name,
            'division': subject.division,
            'score': subject.score,
            'condition': subject.condition,
            'theory_ddhhhh': subject.theory_ddhhhh,
            'theory_professor': subject.theory_professor,
            'practice_ddhhhh': subject.practice_ddhhhh,
            'practice_professor': subject.practice_professor,
            'exams': subject.serialize_list(subject.exams),
            'tasks': subject.serialize_list(subject.tasks),
        })
        return dict(status="ok", data=dict(subjects=final_subjects))
    return dict(status="error", msg="Request not allowed")


# TASK METHODS


@users.route('/task', methods=["POST", "DELETE", "PUT"])
@jwt_required
def task():
    if request.method == "POST":
        description = request.json.get("description", None)
        date = request.json.get("date", None)
        score = request.json.get("score", None)
        is_done = request.json.get("isDone", None)
        subject_id = request.json.get("subjectId", None)

        registered_task = register_task(
            description,
            date,
            score,
            is_done,
            subject_id
        )
        if registered_task['status'] == "ok":
            return dict(status="ok", task=registered_task['data'])
        return dict(status="error", msg=registered_task['msg'])

    if request.method == "DELETE":
        task_id_delete = request.json.get("id", None)
        task_to_delete = Task.query.filter_by(id=task_id_delete).first()
        if task_to_delete is not None:
            if delete_task(task_to_delete):
                return dict(status="ok")
            return dict(status="error", msg="task not deleted")
        return dict(status="error", msg="task not found")

    if request.method == "PUT":
        task_id_put = request.json.get("id", None)
        description = request.json.get("description", None)
        date = request.json.get("date", None)
        score = request.json.get("score", None)
        is_done = request.json.get("isDone", None)

        if is_task_id_valid(task_id_put):
            if modify_task(
                task_id_put,
                description,
                date,
                score,
                is_done,
            ):
                return dict(status="ok")
            return dict(status="error", msg="task not updated")
        return dict(status="error", msg="task not found")
    return dict(status="error", msg="request not allowed")


@users.route('/gettask', methods=["POST"])
@jwt_required
def get_task():
    if request.method == "POST":
        task_id = request.json.get("id", None)
        task = Task.query.filter_by(id=task_id).first()
        if task is None:
            return dict(status="error", msg="Task not found")
        return dict(status="ok", data=dict(task=task.serialize()))
    return dict(status="error", msg="Request not allowed")


@users.route('/tasksbysubject', methods=["POST"])
@jwt_required
def get_tasksbysubject():
    if request.method == "POST":
        subject_id_get_task = request.json.get("id", None)
        if is_subject_id_valid(subject_id_get_task):
            tasks = Task.query.filter_by(subject_id=subject_id_get_task).all()
            return dict(status="ok", data=dict(tasks=Task.serialize_list(elements=tasks)))
        return dict(status="error", msg="subject id not found")
    return dict(status="error", msg="Request not allowed")


@users.route('/tasks', methods=["GET"])
@jwt_required
def get_tasks():
    if request.method == "GET":
        tasks = Task.query.all()
        return dict(status="ok", data=dict(tasks=Task.serialize_list(elements=tasks)))
    return dict(status="error", msg="Request not allowed")


# EXAMS METHODS


@users.route('/exam', methods=["POST", "DELETE", "PUT"])
@jwt_required
def exam():
    if request.method == "POST":
        description = request.json.get("description", None)
        date = request.json.get("date", None)
        score = request.json.get("score", None)
        subject_id = request.json.get("subjectId", None)

        registered_exam = register_exam(
            description,
            date,
            score,
            subject_id
        )
        if registered_exam['status'] == "ok":
            return dict(status="ok", exam=registered_exam['data'])
        return dict(status="error", msg=registered_exam['msg'])

    if request.method == "DELETE":
        exam_id_delete = request.json.get("id", None)
        exam_to_delete = Exam.query.filter_by(id=exam_id_delete).first()
        if exam_to_delete is not None:
            if delete_exam(exam_to_delete):
                return dict(status="ok")
            return dict(status="error", msg="exam not deleted")
        return dict(status="error", msg="exam not found")

    if request.method == "PUT":
        exam_id_put = request.json.get("id", None)
        description = request.json.get("description", None)
        date = request.json.get("date", None)
        score = request.json.get("score", None)

        if is_exam_id_valid(exam_id_put):
            if modify_exam(
                exam_id_put,
                description,
                date,
                score,
            ):
                return dict(status="ok")
            return dict(status="error", msg="exam not updated")
        return dict(status="error", msg="exam not found")
    return dict(status="error", msg="request not allowed")


@users.route('/getexam', methods=["POST"])
@jwt_required
def get_exam():
    if request.method == "POST":
        exam_id = request.json.get("id", None)
        exam = Exam.query.filter_by(id=exam_id).first()
        if exam is None:
            return dict(status="error", msg="Exam not found")
        return dict(status="ok", data=dict(exam=exam.serialize()))
    return dict(status="error", msg="Request not allowed")


@users.route('/examsbysubject', methods=["POST"])
@jwt_required
def get_examsbysubject():
    if request.method == "POST":
        subject_id_get_exam = request.json.get("id", None)
        if is_subject_id_valid(subject_id_get_exam):
            exams = Exam.query.filter_by(subject_id=subject_id_get_exam).all()
            return dict(status="ok", data=dict(exams=Exam.serialize_list(elements=exams)))
        return dict(status="error", msg="subject id not found")
    return dict(status="error", msg="Request not allowed")


@users.route('/exams', methods=["GET"])
@jwt_required
def get_exams():
    if request.method == "GET":
        exams = Exam.query.all()
        return dict(status="ok", data=dict(exams=Exam.serialize_list(elements=exams)))
    return dict(status="error", msg="Request not allowed")
