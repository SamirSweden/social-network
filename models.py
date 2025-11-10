from sqlalchemy import Column , Integer , String , Text , DateTime , ForeignKey , Boolean 
from sqlalchemy.orm import relationship 
from sqlalchemy.sql import func

from database import Base


class User(Base):
    __tablename__ = "users" 

    id = Column(Integer , primary_key=True, index=True)
    username = Column(String(50) , unique=True , index=True , nullable=False)
    email = Column(String(100) , unique=True , index=True, nullable=False)
    hashed_password = Column(String , nullable=False)
    is_active = Column(Boolean , default=True)
    created_at = Column(DateTime(timezone=True) , server_default=func.now())

    posts = relationship("Post" , back_populates="author")


class Post(Base):
    __tablename__ = "posts" 

    id = Column(Integer , primary_key=True, index=True)
    author_id = Column(Integer , ForeignKey("users.id") , nullable=False)
    content = Column(Text , nullable=False)
    created_at = Column(DateTime(timezone=True) , server_default=func.now())


    author = relationship("User" , back_populates="posts")
