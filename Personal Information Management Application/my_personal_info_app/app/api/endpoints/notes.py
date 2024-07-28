from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import NoteCreate, NoteResponse
from app.crud import create_note, get_notes
from app.dependencies import get_db

router = APIRouter()

@router.post("/notes/", response_model=NoteResponse)
def create_new_note(note: NoteCreate, db: Session = Depends(get_db)):
    return create_note(db=db, note=note)

@router.get("/notes/", response_model=list[NoteResponse])
def read_notes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    notes = get_notes(db, skip=skip, limit=limit)
    return notes