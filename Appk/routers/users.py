from fastapi import FastAPI, Response,status, HTTPException, Depends, APIRouter
import models, schema, utils
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(
    prefix="/user",
    tags= ['user']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.userout)
def create_user(user: schema.usercreate,
                db: Session = Depends(get_db)):
    
    #hash the password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.get("/", response_model=list[schema.userout])
def get_user_OP(db: Session = Depends(get_db)):
    user = db.query(models.User).all()
    
    
    return user

router.get("/{id}", response_model=schema.userout)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail= "user not found")
    
    return user