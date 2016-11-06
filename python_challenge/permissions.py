"""
This contains most of the logic for user authentication (login) as
well as user role handling.
"""

from flask import session, redirect, url_for
from functools import wraps
import hashlib


from python_challenge import app, mongo, SALT


def authenticate(username, password):
    """Authentice with the database"""
    hashed_password = hashlib.sha512(password + SALT).hexdigest()
    user = mongo.db.users.find_one({'username': username}) # Don't send the hashed password through logs
    
    if user is not None and user["password"] == hashed_password:
        return True
    return False


def get_current_user_permissions():
    """Access the database and return a tuple of user permissions."""
    user = mongo.db.users.find_one({'username': session['username']})
    if user is not None:
        return [k for k in user.keys() if user[k] == True]
    return []
    
    
def error_response():
    """Return error message for incorrect permissions.
    
    This should be so much nicer."""
    return "Invalid permissions"
    

def requires(permission):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            try:
                if permission not in get_current_user_permissions():
                    return error_response()
            except KeyError:
                return redirect(url_for("index"))
            return f(*args, **kwargs)
        return wrapped
    return wrapper
