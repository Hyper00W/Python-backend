```
 ⚔️  _____         _   ___    _   _   ___ 
     / ___/        | | / _ \  | | | | |_ _|
     \___ \        | || | | | | |_| |  | | 
      ___) |  ___  | || |_| | |  _  |  | | 
     |____/  (___) |_| \___/  |_| |_| |___|
                                          
     🚀 FastAPI Training Arc
     Backend Development Learning Journey
```

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green?style=flat-square&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-336791?style=flat-square&logo=postgresql)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Learning%20Project-orange?style=flat-square)

**A hands-on learning project to master REST API development with FastAPI and PostgreSQL**

⭐ Perfect for developers starting their backend development journey

</div>

---

## 📚 Table of Contents

- [Overview](#overview)
- [Project Purpose](#project-purpose)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Installation Guide](#installation-guide)
- [Usage Guide](#usage-guide)
- [Learning Objectives](#learning-objectives)
- [Potential Improvements](#potential-improvements)
- [Author](#author)

---

## 🎯 Overview

**FastAPI Training Arc** is a learning project designed to practice and understand the fundamentals of backend development using FastAPI. This project implements a simple but complete REST API for managing blog posts with a PostgreSQL database backend.

### Key Purpose
- 📖 **Learning focused** - Built while studying Python backend development
- 🎓 **Educational value** - Demonstrates core FastAPI concepts
- 🏗️ **Not production-ready** - Intended as a learning tool, not for production use
- 💡 **Hands-on practice** - Real-world API patterns in a manageable scope

---

## ✨ Features

### Core Functionality
- ✅ **Post Management** - Create, read, update, and delete blog posts
- ✅ **RESTful API Design** - Standard REST conventions for API endpoints
- ✅ **Data Validation** - Pydantic models for request/response validation
- ✅ **Database Integration** - PostgreSQL with persistent data storage
- ✅ **Error Handling** - HTTP status codes and exception handling
- ✅ **Connection Management** - Automatic database connection with retry logic

---

## 🛠️ Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Framework** | FastAPI | 0.104+ |
| **Language** | Python | 3.9+ |
| **Database** | PostgreSQL | 13+ |
| **ORM/Driver** | psycopg2 | Latest |
| **Validation** | Pydantic | Built-in with FastAPI |

---

## 📁 Project Structure

```
FCC/
├── main.py                 # Main FastAPI application and routes
├── venv/                   # Python virtual environment
└── README.md              # This file
```

### File Descriptions

| File | Purpose |
|------|---------|
| `main.py` | Contains FastAPI app initialization, database connection, data models, and all API endpoints |

---

## 🌐 API Endpoints

### Base URL
```
http://localhost:8000
```

### Endpoints Documentation

#### 1. **Root Endpoint**
```http
GET /
```
- **Description**: Health check / welcome endpoint
- **Response**: 
  ```json
  {
    "Hello": "World"
  }
  ```

#### 2. **Get All Posts**
```http
GET /posts
```
- **Description**: Retrieve all posts from the database
- **Status Code**: 200 OK
- **Response**:
  ```json
  {
    "data": [
      {
        "id": 1,
        "title": "Post Title",
        "content": "Post content here",
        "published": true
      }
    ]
  }
  ```

#### 3. **Create New Post**
```http
POST /createpost
```
- **Description**: Create a new blog post
- **Status Code**: 201 Created
- **Request Body**:
  ```json
  {
    "title": "New Post Title",
    "content": "Post content",
    "published": true
  }
  ```
- **Response**: Created post with ID

#### 4. **Get Latest Post**
```http
GET /posts/latest
```
- **Description**: Retrieve the most recently added post
- **Status Code**: 200 OK
- **Response**:
  ```json
  {
    "detals": {
      "id": 2,
      "title": "Favourite Foods",
      "content": "I Like Chicken"
    }
  }
  ```

#### 5. **Get Post by ID**
```http
GET /posts/{id}
```
- **Description**: Retrieve a specific post by its ID
- **Parameters**: 
  - `id` (integer): Post ID
- **Status Code**: 200 OK (or 404 if not found)
- **Response**:
  ```json
  {
    "data": {
      "id": 1,
      "title": "Post Title",
      "content": "Content here",
      "published": true
    }
  }
  ```

#### 6. **Update Post**
```http
PUT /posts/{id}
```
- **Description**: Update an existing post
- **Parameters**: 
  - `id` (integer): Post ID
- **Status Code**: 200 OK (or 404 if not found)
- **Request Body**:
  ```json
  {
    "title": "Updated Title",
    "content": "Updated content",
    "published": true
  }
  ```
- **Response**: Updated post object

#### 7. **Delete Post**
```http
DELETE /posts/{id}
```
- **Description**: Delete a post by ID
- **Parameters**: 
  - `id` (integer): Post ID
- **Status Code**: 204 No Content (or 404 if not found)
- **Response**: No content on success

---

## 🚀 Installation Guide

### Prerequisites
- Python 3.9 or higher
- PostgreSQL 13 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd FCC
```

### Step 2: Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install fastapi
pip install uvicorn
pip install pydantic
pip install psycopg2-binary
```

### Step 4: Configure Database
1. Create a PostgreSQL database:
   ```sql
   CREATE DATABASE fastapi;
   ```

2. Create the posts table:
   ```sql
   CREATE TABLE posts (
     id SERIAL PRIMARY KEY,
     title VARCHAR(255) NOT NULL,
     content TEXT NOT NULL,
     published BOOLEAN DEFAULT TRUE,
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

3. Update database credentials in `main.py`:
   ```python
   conn = psycopg2.connect(
       host='localhost',
       database='fastapi',
       user='postgres',
       password='your_password',  # Change this
       cursor_factory=RealDictCursor
   )
   ```

---

## 💻 Usage Guide

### Running the Application

```bash
# Start the FastAPI server
uvicorn main:app --reload
```

The server will start at: `http://localhost:8000`

### Interactive API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Example Requests

**Create a post:**
```bash
curl -X POST "http://localhost:8000/createpost" \
  -H "Content-Type: application/json" \
  -d '{"title":"My First Post","content":"This is awesome!","published":true}'
```

**Get all posts:**
```bash
curl "http://localhost:8000/posts"
```

**Get post by ID:**
```bash
curl "http://localhost:8000/posts/1"
```

**Update a post:**
```bash
curl -X PUT "http://localhost:8000/posts/1" \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated Title","content":"Updated content","published":true}'
```

**Delete a post:**
```bash
curl -X DELETE "http://localhost:8000/posts/1"
```

---

## 🎓 Learning Objectives

This project covers and reinforces understanding of:

### Core Concepts
- ✅ **FastAPI Fundamentals** - Framework setup, routing, and request handling
- ✅ **REST API Design** - RESTful principles and HTTP methods (GET, POST, PUT, DELETE)
- ✅ **Data Models** - Pydantic models for data validation and serialization
- ✅ **HTTP Status Codes** - Appropriate status code usage (200, 201, 204, 404, etc.)
- ✅ **Exception Handling** - HTTPException for error responses

### Advanced Topics
- ✅ **Database Integration** - SQL queries and database connections
- ✅ **Path Parameters** - Dynamic routing with URL parameters
- ✅ **Request Bodies** - JSON request validation and parsing
- ✅ **Connection Management** - Retry logic and persistent connections
- ✅ **Type Hints** - Python type annotations for code clarity

---

## 🔮 Potential Improvements

As a learning project, there are several areas that could be enhanced in future iterations:

### Code Quality
- [ ] **Separation of Concerns** - Move database logic to a separate layer (repositories/DAOs)
- [ ] **Configuration Management** - Use environment variables for database credentials
- [ ] **Connection Pooling** - Implement connection pooling instead of single connection
- [ ] **Error Handling** - More granular exception handling and logging
- [ ] **Input Validation** - Additional validation for edge cases

### Features
- [ ] **Authentication** - Add user authentication and authorization
- [ ] **Pagination** - Implement pagination for list endpoints
- [ ] **Filtering & Sorting** - Add query parameters for filtering and sorting
- [ ] **Timestamps** - Add created_at and updated_at fields
- [ ] **Search** - Full-text search capability for posts

### Architecture
- [ ] **SQLAlchemy ORM** - Replace raw SQL with ORM for better maintainability
- [ ] **Dependency Injection** - Use FastAPI's dependency injection system
- [ ] **Middleware** - Add logging, CORS, and security middleware
- [ ] **Unit Tests** - Implement comprehensive test suite
- [ ] **Docker** - Containerize the application

### DevOps
- [ ] **Database Migrations** - Use Alembic for schema versioning
- [ ] **Async Operations** - Convert to async/await for better performance
- [ ] **API Documentation** - Enhanced documentation with examples
- [ ] **CI/CD Pipeline** - GitHub Actions or similar for automated testing

---

## 👤 Author

**Aditya Manhas**

This project was created as part of a FastAPI learning journey to understand backend development fundamentals.

### Notes
- 🎓 This is a **learning project**, not meant for production use
- 📚 Built while studying Python backend development
- 🚀 Feel free to fork, modify, and use as a learning resource

---

## 📝 License

This project is provided as an educational resource.

---

<div align="center">

**Made with ⚔️ dedication to learning FastAPI**

*"The only way to learn a new programming paradigm is by writing programs in it."* - Alan J. Perlis

</div>
