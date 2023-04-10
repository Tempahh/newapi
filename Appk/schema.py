from pydantic import BaseModel, EmailStr, conint
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
   ##created_at: datetime
    
    class Config:
        orm_mode = True

class postty(PostBase):
    id :  int
    created_at :  datetime
    ##owner_id : int
    owner : userout
    
    class Config:
        orm_mode = True

class postout(BaseModel):
    media: postty
    votes: int
    
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


class Vote(BaseModel):
    media_id: int
    dir: conint(le=1) # type: ignore
    
