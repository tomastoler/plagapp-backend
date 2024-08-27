from flask import Blueprint, jsonify, redirect, url_for
from ..data.users import Users
from flask_login import current_user


admin = Blueprint('admin', __name__)

def is_admin(func):
    def wrapper(*args, **kwargs):
        if current_user.role != 'ADMIN':
            return redirect(url_for('auth.unauthorized'))
        return func(*args, **kwargs)
    return wrapper

@admin.route('/users')
@is_admin
def users():
    return jsonify({ "users": list(map(lambda user: user.to_dict(), Users.get_all())) }), 200