from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models
from app import database
from app.database import engine
from app.routers import post, user, auth, vote
from app.config import settings


# models.Base.metadata.create_all(bind=engine) --> We don't need this command anymore as we are using alembic to create the tables   

app = FastAPI()

origins = ["*"]  # list of domains that can talk to our api
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Hello World!!!!!"}