from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

import models
from database import SessionLocal

app = FastAPI()

# Pydantic model
class PostCreate(BaseModel):
    title: str
    body: str
    userId: int

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# TEST ROUTE (IMPORTANT)
@app.get("/")
def root():
    return {"message": "API working"}

# CREATE ROUTE
@app.post("/posts")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post