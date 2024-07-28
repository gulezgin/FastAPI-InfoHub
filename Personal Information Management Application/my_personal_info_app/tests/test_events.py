from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_event():
    response = client.post("/events/", json={"title": "Test Event", "description": "This is a test event.", "event_date": "2024-08-01T12:00:00"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Event"
    assert response.json()["description"] == "This is a test event."

def test_read_events():
    response = client.get("/events/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
