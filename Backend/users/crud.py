from sqlalchemy.orm import Session
from database.models import User

def get_user_by_email(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    user_name = user.role
    print(f'User Role of email {email}: {user_name}')
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, email: str, hashed_password: str, role: str = "student"):
    user = User(email=email, hashed_password=hashed_password, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    print(db.query(User).filter)
    return user
