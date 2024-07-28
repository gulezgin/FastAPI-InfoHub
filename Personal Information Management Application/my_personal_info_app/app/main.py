from fastapi import FastAPI
from .db.base import Base
from .db.session import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome44."}

from .api.endpoints import users, notes, tasks, events

app.include_router(users.router)
app.include_router(notes.router)
app.include_router(tasks.router)
app.include_router(events.router)