from email.policy import HTTP
from .. import models, schemas, oauth2
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session  
from ..database import get_db
from typing import List, Optional

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
    )

@router.get("/", response_model=List[schemas.Post])
async def get_posts(db: Session = Depends(get_db), 
            current_user: int = Depends(oauth2.get_current_user),
             limit: int = 10, skip: int = 0, search: Optional[str] = ""):
   # cursor.execute(""" SELECT * FROM posts """)
   # posts = cursor.fetchall()
   #To get our own user post 
    #posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
    
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit=limit).offset(skip).all()

    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
async def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), 
                        current_user: int = Depends(oauth2.get_current_user)):
   # cursor.execute(""" INSERT INTO posts (title, content, published)
  #          VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
   # new_post = cursor.fetchone()

  #  conn.commit()

        #new_post = models.Post(title=post.title, content=post.content, published=post.published)
        #print(**post.dict()) #convert post into a dictionary
        #print(current_user.email)
        new_post = models.Post(owner_id=current_user.id, **post.dict())

        db.add(new_post)
        db.commit()
        db.refresh(new_post)
    
        return new_post

@router.get("/{id}")
async def get_post(id: int, db: Session = Depends(get_db), response_model=schemas.Post,
                        current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id)),)
    # post = cursor.fetchone()
    # print(post)

    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"message": f"post with id {id} was not found"}
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db), 
                            current_user: int = Depends(oauth2.get_current_user)):
    #deleting post
    #find the index of the id to delete 
    #make my_posts.pop() to remove the index
    # cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)),)
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Post)
async def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" UPDATE posts SET title = %s, content=%s, published=%s 
    # WHERE id = %s RETURNING *""", 
    # (post.title, post.content, post.published, id))
    # updated_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()

#title str, content str