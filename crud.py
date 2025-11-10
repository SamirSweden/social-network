# crud.py
from sqlalchemy.orm import Session
from models import User, Post

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 

def get_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, username: str, email: str, password: str):
    hashed_password = password 
    db_user = User(username=username, email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()

def create_post(db: Session, content: str, author_id: int):
    db_post = Post(content=content, author_id=author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
