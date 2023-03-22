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



while True:    
    try:
        conn = psycopg2.connect(host='localhost', database='newapi', user='postgres', password='204682', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connect successful!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth0.router)


@app.get("/")
def root():
    return {'message':'Hello World'}


