# Production API Platform

A production-ready REST API built with FastAPI, PostgreSQL, JWT Authentication, Docker, and deployed on Render.

## Live Demo

**Production URL**

https://production-api-platform.onrender.com

**Swagger Documentation**

https://production-api-platform.onrender.com/docs

---

## Project Overview

This project demonstrates how to build, containerize, and deploy a production-grade backend application.

The API provides:

* User Registration
* User Login
* JWT Authentication
* Protected Routes
* Product Management APIs
* PostgreSQL Database Integration
* Dockerized Deployment
* Cloud Deployment using Render

---

## Features

### Authentication

* User Registration
* User Login
* JWT Token Generation
* OAuth2 Password Flow
* Protected Endpoints

### Products

* Fetch Product Details
* Database-backed Product Storage

### Infrastructure

* Docker Containerization
* Docker Compose Setup
* PostgreSQL Database
* Environment Variable Configuration
* Cloud Deployment

---

## Tech Stack

### Backend

* FastAPI
* Python 3.13
* SQLAlchemy
* Pydantic

### Authentication

* JWT
* OAuth2
* Passlib (bcrypt)

### Database

* PostgreSQL
* Neon PostgreSQL (Cloud)

### DevOps

* Docker
* Docker Compose
* GitHub
* Render

---

## Project Structure

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
│   │
│   └── repositories/
│       ├── user_repository.py
│       └── product_repository.py
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .env
│
└── README.md
```

---

## Architecture

```text
Client
   │
   ▼
FastAPI Routes
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
SQLAlchemy ORM
   │
   ▼
PostgreSQL Database
```

---

## API Endpoints

### Authentication

| Method | Endpoint  | Description              |
| ------ | --------- | ------------------------ |
| POST   | /register | Register a new user      |
| POST   | /login    | Login user               |
| POST   | /token    | Generate JWT Token       |
| GET    | /profile  | Get current user profile |

### Products

| Method | Endpoint  | Description      |
| ------ | --------- | ---------------- |
| GET    | /products | Get all products |

---

## Local Setup

### Clone Repository

```bash
git clone https://github.com/GowthamK2/Production-api-platform.git
cd Production-api-platform
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://username:password@localhost/db_name

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Run Locally

```bash
uvicorn app.main:app --reload
```

Application:

```text
http://localhost:8000
```

Swagger Docs:

```text
http://localhost:8000/docs
```

---

## Docker Setup

### Build Image

```bash
docker build -t production-api-platform .
```

### Run Container

```bash
docker run -p 8000:8000 production-api-platform
```

---

## Docker Compose

### Start Services

```bash
docker compose up --build
```

### Stop Services

```bash
docker compose down
```

---

## Deployment

### Render

Application deployed using:

* Render Web Service
* Docker Runtime
* Neon PostgreSQL Database

Live URL:

https://production-api-platform.onrender.com

---

## Testing

Run tests:

```bash
pytest
```

---

## Future Improvements

* CI/CD using GitHub Actions
* Product CRUD Operations
* Role Based Access Control (RBAC)
* Redis Caching
* Rate Limiting
* Monitoring & Logging
* Kubernetes Deployment

---

## Author

**Gowtham K**

GitHub:
https://github.com/GowthamK2
