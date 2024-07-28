from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import EventCreate, EventResponse
from app.crud import create_event, get_events
from app.dependencies import get_db


router = APIRouter()

@router.post("/events/", response_model=EventResponse)
def create_new_event(event: EventCreate, db: Session = Depends(get_db)):
    return create_event(db=db, event=event)

@router.get("/events/", response_model=list[EventResponse])
def read_events(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    events = get_events(db, skip=skip, limit=limit)
    return events
