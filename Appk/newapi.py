from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from database import engine
import models
from models import *
from routers import posts, users, auth0


models.Base.metadata.create_all(bind=engine)


app = FastAPI()





app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth0.router)


@app.get("/")
def root():
    return {'message':'Hello World'}


