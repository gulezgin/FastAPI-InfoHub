from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import TaskCreate, TaskResponse
from app.crud import create_task, get_tasks
from app.dependencies import get_db

router = APIRouter()

@router.post("/tasks/", response_model=TaskResponse)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db=db, task=task)

@router.get("/tasks/", response_model=list[TaskResponse])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = get_tasks(db, skip=skip, limit=limit)
    return tasks
