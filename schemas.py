from pydantic import BaseModel 
from typing import List , Optional
from datetime import datetime 


class UserBase(BaseModel):
    username : str 
    email : str


class UserCreate(UserBase):
    password : str


class User(UserBase):
    id: int  
    is_active: bool 
    created_at: datetime

    class Config: 
        from_attributes=True

class PostBase(BaseModel):
    content: str 

class PostCreate(PostBase):
    pass 


class Post(PostBase):
    id: int  
    is_active: bool 
    created_at: datetime

    author: User

    class Config:
        from_attributes=True

