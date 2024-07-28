from fastapi.testclient import TestClient
from app.main import app
from app.schemas import UserCreate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})
SessionLocal =sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "testuser", "email": "testuser@examğle.com", "full_name": "Test User"})
    assert response.status_code==200
    assert response.json()["username"]== "testuser"
    assert response.json()["email"]== "testuser@example.com"

def test_read_users():
    response = client.get("/users/")
    assert response.status_code==200
    assert isinstance(response.json(), list)

