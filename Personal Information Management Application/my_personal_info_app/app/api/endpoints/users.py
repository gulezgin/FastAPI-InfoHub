from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import UserCreate, User
from app.crud import create_user, get_users
from app.dependencies import get_db

router = APIRouter()

@router.post("/users/", response_model=User)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@router.get("/users/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit= limit)
    return users

