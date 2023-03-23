from fastapi import status, HTTPException, Depends, APIRouter
import models, schema
from sqlalchemy.orm import Session
from database import get_db
from typing import List
from . import auth01

router = APIRouter(
    prefix="/posts",
    tags= ['posts']
)

@router.get("/", response_model= List[schema.postty])
def test_posts(db: Session = Depends(get_db), cur_user: int = Depends(auth01.get_user)):
    posts = db.query(models.media).filter(
        models.media.owner_id == cur_user.id).all()  # type: ignore
    return posts




@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.postty)
def create_posts(post: schema.PostCreate, db: Session = Depends(get_db), cur_user: int = Depends(auth01.get_user)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
    #                (post.title, post.content, post.published))
    # new_post = cursor.fetchone()

    # conn.commit()

    new_post = models.media(owner_id=cur_user.id, **post.dict()) # type: ignore
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post




@router.get("/{id}")
def get_post(id: int, db: Session = Depends(get_db),cur_user: int = Depends(auth01.get_user)):
    #cursor.execute("""SELECT * FROM media WHERE id = %s""", (str(id),))
    #post = cursor.fetchone()
    post = db.query(models.media).filter(models.media.id == id).first() 
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id {id} not found")
    
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), cur_user: int = Depends(auth01.get_user)):
    
    post_query = db.query(models.media).filter(models.media.id == id)
    
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id {id} not found")
        
    if post.owner_id != cur_user.id: # type: ignore
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not authorized")
    
    post_query.delete(synchronize_session=False)
    db.commit()


@router.put("/{id}", response_model=schema.postty)
def edit_post(id: int, Media:schema.PostCreate, db: Session = Depends(get_db),cur_user: int = Depends(auth01.get_user)):
    #cursor.execute("""UPDATE media SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", 
                   #(post.title, post.content, post.published, str(id)))
    
    #updated_post = cursor.fetchone()
    #conn.commit()
    media_query = db.query(models.media).filter(models.media.id == id)
    post = media_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id {id} not found")
        
    if post.owner_id != cur_user.id: # type: ignore
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not authorized")
    
    media_query.update(Media.dict(), synchronize_session=False) # type: ignore
    
    db.commit()
    
    return media_query.first()



