from functools import wraps
from flask import g, redirect,url_for
from sqlalchemy.sql.functions import current_user


def login_required(func):
    #保留func信息
    @wraps(func)
    def inner(*args, **kwargs):
        if g.user:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("auth.login"))
    return inner


