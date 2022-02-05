#from msilib import schema
from turtle import title
from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from importlib_metadata import Deprecated
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session  
from app import models, schemas, utils
from app.database import engine, get_db
from app.routers import post, user, auth


models.Base.metadata.create_all(bind=engine)    

app = FastAPI()

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

        posts = db.query(models.Post).all()

        return posts

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

