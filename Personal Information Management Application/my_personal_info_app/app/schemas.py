from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode=True

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteResponse(NoteBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode= True

class TaskBase(BaseModel):
    title: str
    description: Optional[str]=None
    is_completed: Optional[bool]=False

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class EventBase(BaseModel):
    title: str
    description: Optional[str]=None
    event_date: datetime

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True