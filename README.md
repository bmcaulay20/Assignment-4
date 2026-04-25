# Assignment 4 — FastAPI + MongoDB + User Login

This project extends the mid‑term FastAPI application by integrating **MongoDB** for persistent data storage and implementing a complete **user authentication system**. The backend uses FastAPI with Motor (async MongoDB driver), and the frontend uses simple HTML/JS pages for signup, login, and interacting with protected API routes.

---

## Features

### MongoDB Integration
- Uses **Motor** for async database access  
- Stores users and app data in MongoDB  
- Replaces all in‑memory objects from the mid‑term app  

### User Authentication
- User registration  
- Secure password hashing with **bcrypt**  
- Login with **JWT tokens**  
- Protected routes requiring valid tokens  

### Frontend
- `login.html` and `signup.html`  
- JavaScript `fetch()` calls to backend  
- Stores JWT token in `localStorage`  
- Fully functional login + create account flow  

---

## Required Packages

Install all dependencies with:

```bash
pip install fastapi uvicorn motor python-jose passlib[bcrypt] python-dotenv
```

### Package Breakdown

| Package | Purpose |
|--------|---------|
| fastapi | API framework |
| uvicorn | ASGI server |
| motor | Async MongoDB driver |
| python-jose | JWT creation/verification |
| passlib[bcrypt] | Password hashing |
| python-dotenv | Environment variable loading |

---

## Project Structure

```
Assignment4/
│
├── backend/
│   ├── main.py
│   ├── auth_routes.py
│   ├── database.py
│   ├── models.py
│   ├── utils.py
│
├── frontend/
│   ├── login.html
│   ├── signup.html
│   ├── app.html
│   ├── script.js
│
└── README.md
```

---

## Running the Project

### 1. Start MongoDB  
If installed locally:

```bash
mongod
```

### 2. Start FastAPI Backend  
From the project root:

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Open the Frontend  
Visit:

```
http://localhost:8000/login.html
```

---

## Authentication Endpoints

### POST /auth/register  
Creates a new user with hashed password.

### POST /auth/login  
Returns a JWT token:

```json
{
  "access_token": "<token>"
}
```

### Protected Routes  
Require:

```
Authorization: Bearer <token>
```


## Submission  
Push all code to GitHub and submit the repository URL.
