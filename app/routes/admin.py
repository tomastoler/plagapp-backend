from flask import Blueprint, jsonify, redirect, url_for
from ..data.users import Users
from flask_login import current_user


admin = Blueprint('admin', __name__)

@admin.route('/users')
def users():
    if current_user.role != 'ADMIN':
        return redirect(url_for('auth.unauthorized'))
    return jsonify({ "users": list(map(lambda user: user.to_dict(), Users.get_all())) }), 200


@admin.route('/user/<int:user_id>')
def user(user_id: int = 0):
    if current_user.role != 'ADMIN':
        return redirect(url_for('auth.unauthorized'))
    return jsonify({ "user": Users.get_by_id(user_id) }), 200