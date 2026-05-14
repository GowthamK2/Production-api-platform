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

def test_projects():
    response = client.get("/projects")
    assert response.status_code == 200

def test_get_product():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == {
        "products": ["Laptop", "Keyboard"]
    }


def test_create_user():
    response = client.post("/users", 
                           json = {
                               "name": "Gowtham",
                               "age": 25,
                               "skills": ["FastAPI", "Python"]
                           }
                        )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User Created"
    assert data["data"]["name"] == "Gowtham"

def test_create_product():
    response = client.post(
        "/products",
        json= {
                "name": "Laptop",
                "price": 299999.00,
                "stock": 54
            }
        )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Product Created"
    assert data["data"]["name"] == "Laptop" 
