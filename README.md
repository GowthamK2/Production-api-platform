# 🚀 Production API Platform

A production-ready REST API built with FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, Docker, and Docker Compose.

## 📌 Overview

Production API Platform is a backend service that demonstrates modern backend engineering practices including:

* User Authentication with JWT
* OAuth2 Authorization
* Product Management APIs
* PostgreSQL Database Integration
* Repository Pattern Architecture
* Logging & Middleware
* Environment Variable Management
* Docker Containerization
* Docker Compose Orchestration

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic

### Database

* PostgreSQL

### Authentication

* JWT (JSON Web Tokens)
* OAuth2 Password Flow

### DevOps

* Docker
* Docker Compose

### Testing

* Pytest

---

## 📂 Project Structure

```text
production-api-platform/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── services.py
│   ├── security.py
│   └── repositories/
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

## ✨ Features

### Authentication

* User Registration
* User Login
* JWT Token Generation
* Protected Endpoints
* OAuth2 Integration

### Product Management

* Create Product
* Get Products
* Get Product By ID
* Delete Product

### Production Features

* Logging Middleware
* Request Timing Middleware
* Environment Variables
* Repository Pattern
* Async Endpoints

---

## 🐳 Running with Docker

### Build & Start

```bash
docker compose up --build
```

### Stop

```bash
docker compose down
```

---

## 📖 API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

---

## 🔐 Authentication Flow

1. Register User
2. Login User
3. Receive JWT Token
4. Authorize in Swagger
5. Access Protected Routes

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* REST API Development
* Database Design
* JWT Authentication
* OAuth2 Authorization
* Repository Pattern
* Docker & Docker Compose
* Backend Project Structure
* Production-Ready API Practices

---

## 👨‍💻 Author

Gowtham K

GitHub:
https://github.com/GowthamK2
