from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Force table creation for CI
from app.database import Base, engine
from app.models import Product, User

Base.metadata.create_all(bind=engine)


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

    assert data["name"] == "Laptop"
    assert data["price"] == 50000
    assert data["stock"] == 10

# -----------------------------
# GET ALL PRODUCTS TEST
# -----------------------------

def test_get_products():

    response = client.get("/products")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)


# -----------------------------
# GET SINGLE PRODUCT TEST
# -----------------------------

def test_get_single_product():

    create_response = client.post(
        "/products",
        json={
            "name": "Monitor",
            "price": 10000,
            "stock": 5,
            "description": "Gaming Monitor"
        }
    )

    product_id = create_response.json()["id"]

    response = client.get(
        f"/products/{product_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Monitor"


# -----------------------------
# UPDATE PRODUCT TEST
# -----------------------------

def test_update_product():

    create_response = client.post(
        "/products",
        json={
            "name": "Tablet",
            "price": 20000,
            "stock": 7,
            "description": "Android tablet"
        }
    )

    product_id = create_response.json()["id"]

    response = client.put(
        f"/products/{product_id}",
        json={
            "name": "Gaming Tablet",
            "price": 25000,
            "stock": 5,
            "description": "Gaming tablet"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Product updated"


# -----------------------------
# DELETE PRODUCT TEST
# -----------------------------

def test_delete_product():

    create_response = client.post(
        "/products",
        json={
            "name": "Mouse",
            "price": 1000,
            "stock": 5,
            "description": "Wireless mouse"
        }
    )

    product_id = create_response.json()["id"]

    response = client.delete(
        f"/products/{product_id}"
    )

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