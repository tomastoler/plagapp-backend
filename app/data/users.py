from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db


class Users:
    
    @staticmethod
    def get_by_email(email: str = '') -> User | None:
        return User.query.filter_by(email=email).first()
        
    @staticmethod
    def get_by_id(id: int = 0) -> User | None:
        return User.query.get(id)
        
    @staticmethod
    def create(
        name: str = '',
        lastname: str = '',
        email: str = '',
        password: str = '',
        role: str = 'ADMIN'
    ) -> User:
        user_pswd = Passwords.generate(password)
        new_user = User(
            name=name,
            lastname=lastname,
            email=email,
            password=user_pswd,
            role=role
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
        
class Passwords:
    
    @staticmethod            
    def generate(pswd: str = '') -> str:
        return generate_password_hash(pswd, method="scrypt")

    @staticmethod
    def compare(user_pswd: str = '', hash_pswd: str = '') -> bool:
        return check_password_hash(hash_pswd, user_pswd)
