from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import database, schema, models, utils
from . import auth01

router = APIRouter(
    tags=['authentication']
    )

@router.post('/login', response_model=schema.Token)
def login(user_cred : OAuth2PasswordRequestForm= Depends(),  db: Session= Depends(database.get_db)):
   
   user =  db.query(models.User).filter(models.User.email == user_cred.username).first()

   if not user:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail= 'invalid credentials')


   if not utils.verify(user_cred.password, user.password ):
       raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail='invalid credentials')
   
   access_token = auth01.create_access_token(data= {'user_id': user.id})
   
   return{'access_token': access_token, 'token_type':"bearer"}

