from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
    
    
class PostCreate(PostBase):
    pass

class postty(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    
    class Config:
        orm_mode = True

        

class usercreate(BaseModel):
    email: EmailStr
    password: str
    
class userout(BaseModel):
    owner_id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True
        
class userlogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class Tokeninfo(BaseModel):
    id: int
