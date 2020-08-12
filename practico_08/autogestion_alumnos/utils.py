from flask import redirect, url_for


def go_to(page: str):
    return redirect(url_for(page))
