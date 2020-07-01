from flask import redirect, url_for, session


def go_to(page: str):
    return redirect(url_for(page))


def logged():
    if "userName" in session and "password" in session:
        return True
    return False


def delete_session_information():
    if logged():
        session.pop("userName", None)
        session.pop("password", None)
        session.pop("dni", None)
    return True
