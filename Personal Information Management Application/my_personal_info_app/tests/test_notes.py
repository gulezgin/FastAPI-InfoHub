from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_note():
    response = client.post("/notes/", json={"title": "Test Note", "content": "This is a test note."})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Note"
    assert response.json()["content"] == "This is a test note."

def test_read_notes():
    response = client.get("/notes/")
    assert response.status_code==200
    assert isinstance((response.json(), list))