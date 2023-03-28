from fastapi import Depends, status, HTTPException
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session
import schema, database, models
from fastapi.security import OAuth2PasswordBearer
from config import settings

auth_scheme = OAuth2PasswordBearer(tokenUrl='login')



Secret_key = settings.secret_key
ALGORITHM = settings.algorithm
access_token_expire_minutes_int= (int(settings.access_token_expire_minutes)) # type: ignore

def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(minutes=access_token_expire_minutes_int)
    to_encode.update({'exp': expire})
    
    encoded_jwt = jwt.encode(to_encode, Secret_key, algorithm=ALGORITHM)# type: ignore
    
    return encoded_jwt


def verify_access_token(token: str, cred_exception):
    try:
        payload = jwt.decode(token, Secret_key, algorithms=[ALGORITHM]) # type: ignore
        id: Optional[str] = payload.get('user_id')
        if id is None:
            raise cred_exception
        token_data = schema.Tokeninfo(id=id)
    except JWTError:
        raise cred_exception
    
    return token_data


def get_user(token: str = Depends(auth_scheme), db: Session = Depends(database.get_db)):
    cred_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                   detail='Could not validate credentials',
                                   headers={"WWW-Authenticate": "Bearer"})
    
    token_data = verify_access_token(token, cred_exception)
    
    user = db.query(models.User).filter(models.User.id == token_data.id).first()
    if not user:
        raise cred_exception
    
    return user
