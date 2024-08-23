from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()

DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_DATABASE = os.getenv('POSTGRES_DB')
DB_HOST = os.getenv('POSTGRES_HOST')

def create_app() -> Flask:
    
    app = Flask(__name__, template_folder='templates')
    
    app.secret_key = 'qwertypointasdasdasdasdasd'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_DATABASE}'
    
    db.init_app(app)
    
    # routes / blueprints
    from .routes.auth import auth
    
    app.register_blueprint(auth, url_prefix='/auth')
    
    from .models import User, Certificate
    
    with app.app_context():
        db.create_all()
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.unauthorized'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        print(id)
        return User.query.get(int(id))
    
    CORS(app, supports_credentials=True)
    
    return app