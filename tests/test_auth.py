from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_register_user():

    response = client.post(
        "/register",
        json={
            "username": "testuser123",
            "email": "testuser123@example.com",
            "password": "password123"
        }
    )

    assert response.status_code in [200, 400]


def test_login_user():

    response = client.post(
        "/login",
        json={
            "username": "testuser123",
            "password": "password123"
        }
    )

    assert response.status_code in [200, 401]


def test_token_generation():

    response = client.post(
        "/token",
        data={
            "username": "testuser123",
            "password": "password123"
        },
        headers={
            "Content-Type":
            "application/x-www-form-urlencoded"
        }
    )

    if response.status_code == 200:

        data = response.json()

        assert "access_token" in data

        assert data["token_type"] == "bearer"


def test_profile_without_token():

    response = client.get("/profile")

    assert response.status_code == 401