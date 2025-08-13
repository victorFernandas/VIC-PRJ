from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models_user import User
from schemas_user import UserCreate, UserLogin
from auth import hash_password, verify_password, create_access_token


router = APIRouter()

@router.post("/register")
def register(user : "UserCreate", db : Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not verify_password(user.password, db_user.password):

        raise HTTPException(status_code=401, detail = "Email already registered")
    
    db_user = User(email = user.email, password = hash_password(user.password), role = user.role)
    db.add(db_user)
    db.commit()
    return {"msg":"User created"}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):

        raise HTTPException(status_code= 401, detail = "Invalid credentials")
    
    token = create_access_token(data={"sub" : db_user.email, "role": db_user.role})

    return {"access_token": token, "token_type": "bearer"}


