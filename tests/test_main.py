from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")

    assert response.status_code ==200
    assert response.json() == {"message": "Home route"}

def test_contact():
    response = client.get("/contact")
    assert response.status_code == 200
    assert response.json() == {
        "name" : "Gowtham",
        "role" : "AI Backend Developer"
    }

def test_skills():
    response = client.get("/Skills")
    assert response.status_code == 200
    assert response.json() == {
        "skills": ["FastAPI", "Python"]
    }