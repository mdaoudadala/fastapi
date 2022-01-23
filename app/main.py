from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session  
from .database import engine, SessionLocal
from . import models


models.Base.metadata.create_all(bind=engine)    

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password = 'Mabouly78',
        cursor_factory=RealDictCursor)

        cursor = conn.cursor()
        print("Database connection was successfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error:", error)
        time.sleep(2)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite food",
"content": "i like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/sqlalchemy")
async def test_posts(db: Session = Depends(get_db)):
        return {"status": "success"}

@app.get("/posts")
async def get_posts():
    cursor.execute(""" SELECT * FROM posts """)
    posts = cursor.fetchall()
    #print(posts)
    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
    cursor.execute(""" INSERT INTO posts (title, content, published)
            VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    new_post = cursor.fetchone()

    conn.commit()


    return {"data": new_post}

@app.get("/posts/{id}")
async def get_post(id: int):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id)),)
    post = cursor.fetchone()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"message": f"post with id {id} was not found"}
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    #deleting post
    #find the index of the id to delete 
    #make my_posts.pop() to remove the index
    cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)),)
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_post(id: int, post: Post):
    cursor.execute(""" UPDATE posts SET title = %s, content=%s, published=%s 
    WHERE id = %s RETURNING *""", 
    (post.title, post.content, post.published, id))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} does not exist")

    return {"data": updated_post}

#title str, content str


