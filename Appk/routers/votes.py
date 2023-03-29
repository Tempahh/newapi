from fastapi import FastAPI, Response,status, HTTPException, Depends, APIRouter
import models, schema, database
from sqlalchemy.orm import Session
from database import get_db
from . import auth01

router = APIRouter(
    prefix="/votes",
    tags=["votes"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schema.Vote, db: Session= Depends(database.get_db), cur_user: int = Depends(auth01.get_user)):
    
    post = db.query(models.media).filter(models.media.id == vote.media_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {vote.media_id} does not exist")
    
    vote_query = db.query(models.Vote).filter(
            models.Vote.media_id == vote.media_id, models.Vote.user_id == cur_user.id) # type: ignore
    found_vote = vote_query.first()
    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {cur_user.id} has already voted on post {vote.media_id}") # type: ignore
        new_vote = models.Vote(media_id = vote.media_id, user_id = cur_user.id) # type: ignore
        db.add(new_vote)
        db.commit()
        return{"message":"+1 vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="no new vote")
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        
        return{"message": "deleted vote"}