import dns.rcode
from sqlalchemy.orm import Session
from .models import User, Note, Task, Event
from .schemas import UserCreate, NoteCreate, TaskCreate, EventCreate

def create_uesr(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int=0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def create_note(db: Session, note: NoteCreate):
    db_note = Note(**note.dict())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_notes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Note).offset(skip).limit(limit).all()

def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Task).offset(skip).limit(limit).all()

def create_event(db: Session, event: EventCreate):
    db_event = Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_events(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Event).offset(skip).limit(limit).all()

