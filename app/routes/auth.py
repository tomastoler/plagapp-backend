from flask import Blueprint, request, jsonify
from ..models import User
from ..data.users import Passwords, Users
from flask_login import login_user, logout_user, login_required


auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def sign_up():
    data = request.json
    name = data.get('name')
    lastname = data.get('lastname')
    email = data.get('email')
    password = data.get('password')
    role = "CLIENT"
    
    existing_user = Users.get_by_email(email) 

    if existing_user:
        return jsonify({ "error": "email taken"}), 400
    
    new_user: User = Users.create(name, lastname, email, password, role) 
    login_user(new_user, remember=True)
    return jsonify({ "user": new_user.to_dict() }), 200

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    existing_user: User = Users.get_by_email(email) 
    
    if existing_user and Passwords.compare(password, existing_user.password):
        login_user(existing_user, remember=True)
        return jsonify({ "user": existing_user.to_dict() }), 200
    
    return jsonify({ "message": "credenciales incorrectas" }), 400

@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({ "message": "logged out" }), 200

@auth.route('/unauthorized')
def unauthorized():
    return jsonify({ "message": "Unauthorized" }), 400