from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from database import engine
import models
from routers import posts, users, auth0, votes
from dotenv import load_dotenv


models.Base.metadata.create_all(bind=engine)

load_dotenv()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth0.router)
app.include_router(votes.router)


@app.get("/")
def root():
    return {'message':'Hello World'}


