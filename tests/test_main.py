from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# -----------------------------
# HOME ROUTE TEST
# -----------------------------

def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Production API Platform Running"
    }


# -----------------------------
# CREATE PRODUCT TEST
# -----------------------------

def test_create_product():

    response = client.post(
        "/products",
        json={
            "name": "Laptop",
            "price": 50000,
            "stock": 10,
            "description": "Gaming laptop"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Product added"

    assert data["data"]["name"] == "Laptop"


# -----------------------------
# GET ALL PRODUCTS TEST
# -----------------------------

def test_get_products():

    response = client.get("/products")

    assert response.status_code == 200

    data = response.json()

    assert "products" in data


# -----------------------------
# GET SINGLE PRODUCT TEST
# -----------------------------

def test_get_single_product():

    response = client.get("/products/0")

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Laptop"


# -----------------------------
# UPDATE PRODUCT TEST
# -----------------------------

def test_update_product():

    response = client.put(
        "/products/0",
        json={
            "name": "Gaming Laptop",
            "price": 90000,
            "stock": 5,
            "description": "RTX gaming laptop"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Product updated"


# -----------------------------
# DELETE PRODUCT TEST
# -----------------------------

def test_delete_product():

    client.post(
        "/products",
        json={
            "name": "Mouse",
            "price": 1000,
            "stock": 5,
            "description": "Wireless mouse"
        }
    )

    response = client.delete("/products/1")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Product deleted"


# -----------------------------
# INVALID PRODUCT TEST
# -----------------------------

def test_invalid_product():

    response = client.post(
        "/products",
        json={
            "name": "A",
            "price": -100,
            "stock": -5
        }
    )

    assert response.status_code == 422


# -----------------------------
# INVALID PRODUCT ID TEST
# -----------------------------

def test_invalid_product_id():

    response = client.get("/products/100")

    assert response.status_code == 404