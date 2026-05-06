# Flask Authentication REST API

A production-ready REST API built with **Python** and **Flask** featuring:

- JWT Authentication
- Role-Based Authorization (RBAC)
- SQLite Database
- Secure Password Hashing
- Exception Handling
- Input Validation
- Modular Architecture

This project demonstrates backend engineering best practices and secure API design.

---

## Features

### Authentication
- User Registration
- User Login
- JWT Token Generation
- Protected Routes

### Authorization
- User Roles
- Admin-only Endpoints

### Security
- Password Hashing
- JWT Claims
- Environment Variables

### API Quality
- Standard JSON Responses
- Error Handling
- Health Check Endpoint

---

## Tech Stack

- Python 3.10+
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- SQLite
- Passlib

---

## Project Structure

```bash
flask_auth_api/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── config.py
│   ├── extensions.py
│   └── __init__.py
│
├── run.py
├── requirements.txt
└── .env
```

---

## Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd flask_auth_api
```

Create virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create `.env`

```env
SECRET_KEY=my-secret
JWT_SECRET_KEY=my-jwt-secret
```

---

## Run Application

```bash
python run.py
```

Server starts on:

```bash
http://127.0.0.1:5000
```

---

## Quick Health Check

Open browser:

```bash
http://127.0.0.1:5000/api/health
```

Expected response:

```json
{
  "success": true,
  "message": "API running"
}
```

---

## API Endpoints

### Register User

**POST**

```bash
/auth/register
```

Request:

```json
{
  "username": "admin",
  "password": "123",
  "role": "admin"
}
```

---

### Login

**POST**

```bash
/auth/login
```

Request:

```json
{
  "username": "admin",
  "password": "123"
}
```

Response:

```json
{
  "success": true,
  "token": "JWT_TOKEN"
}
```

---

### Profile

**GET**

```bash
/api/profile
```

Requires:

```bash
Authorization: Bearer <token>
```

---

### Admin

**GET**

```bash
/api/admin
```

Requires admin token.

---

## Test Using Postman

You can test the APIs using:

- Postman
- curl
- Browser (health endpoint)

---

## Common Error Cases

### Duplicate User

```json
{
  "success": false,
  "message": "Username already exists"
}
```

### Invalid Password

```json
{
  "success": false,
  "message": "Invalid password"
}
```

### Missing Token

```json
{
  "msg": "Missing Authorization Header"
}
```

---

## Git Usage

Example commits:

```bash
git init
git add .
git commit -m "Initial Flask API setup"
git commit -m "Added JWT authentication"
```

---

## One-Command Run

After cloning:

```bash
pip install -r requirements.txt && python run.py
```

Windows:

```bash
pip install -r requirements.txt && python run.py
```

Linux/Mac:

```bash
pip3 install -r requirements.txt && python3 run.py
```

---

## Author

Backend API Developer  
Python + Flask + Security + REST APIs

Quick Start (Windows)
Double-click start.bat to launch the API automatically.