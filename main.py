from fastapi import FastAPI, Depends, Header
from sqlalchemy.orm import Session
from pydantic import BaseModel

import models
from database import SessionLocal

import auth_utils
print(dir(auth_utils))
from auth_utils import hash_password, verify_password, create_access_token
from jose import jwt

app = FastAPI()

# ---------------- SCHEMAS ---------------- #

class PostCreate(BaseModel):
    title: str
    body: str
    userId: int

class UserCreate(BaseModel):
    username: str
    password: str

# ---------------- DB ---------------- #

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- BASIC ROUTE ---------------- #

@app.get("/")
def root():
    return {"message": "API working"}

# ---------------- CRUD ---------------- #

@app.post("/posts")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()

# ---------------- AUTH ---------------- #

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    hashed_pw = hash_password(user.password)
    new_user = models.User(username=user.username, password=hashed_pw)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created"}

@app.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()

    if not db_user or not verify_password(user.password, db_user.password):
        return {"error": "Invalid credentials"}

    token = create_access_token({"sub": db_user.username})

    return {"access_token": token, "token_type": "bearer"}

# ---------------- PROTECTED ROUTE ---------------- #

SECRET_KEY = "mysecretkey"

def get_current_user(token: str = Header()):
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    return payload

@app.get("/protected")
def protected(user=Depends(get_current_user)):
    return {"message": "Authorized", "user": user}

