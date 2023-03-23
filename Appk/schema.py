from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
    
    
class PostCreate(PostBase):
    pass

class userout(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True
        
        
class Userout(BaseModel):
    id: int
    email: EmailStr
   ##created_at: datetime
    
    class Config:
        orm_mode = True

class postty(PostBase):
    id :  int
    created_at :  datetime
    ##owner_id : int
    owner : Userout
    
    class Config:
        orm_mode = True

        

class usercreate(BaseModel):
    email: EmailStr
    password: str
           
class userlogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class Tokeninfo(BaseModel):
    id: int
