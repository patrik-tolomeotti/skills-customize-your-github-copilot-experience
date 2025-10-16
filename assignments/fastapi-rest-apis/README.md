# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will learn to build modern REST APIs using the FastAPI framework. By the end of this assignment, you'll understand how to create endpoints, handle different HTTP methods, work with request/response models, and implement basic authentication.

## 📝 Tasks

### 🛠️ Task 1: Setup and Basic API

#### Description
Set up a FastAPI project and create your first API endpoints. You'll build a simple book management system that can handle basic CRUD operations.

#### Requirements
Completed program should:

- Install FastAPI and uvicorn using pip
- Create a main.py file with a FastAPI application
- Implement GET endpoint to retrieve all books
- Implement GET endpoint to retrieve a single book by ID
- Include proper HTTP status codes and response models
- Test the API using the automatic interactive documentation (Swagger UI)

### 🛠️ Task 2: Advanced Operations and Data Validation

#### Description
Extend your API with POST, PUT, and DELETE operations. Implement proper data validation using Pydantic models and handle error cases gracefully.

#### Requirements
Completed program should:

- Create Pydantic models for Book creation and response
- Implement POST endpoint to add new books with validation
- Implement PUT endpoint to update existing books
- Implement DELETE endpoint to remove books
- Add proper error handling for invalid requests (404, 422, etc.)
- Include request/response examples in the API documentation

### 🛠️ Task 3: Authentication and Database Integration

#### Description
Add basic authentication to your API and integrate with a simple database. Implement user registration and protected endpoints.

#### Requirements
Completed program should:

- Set up SQLite database with SQLAlchemy
- Create User and Book database models
- Implement user registration and login endpoints
- Add JWT token-based authentication
- Protect book modification endpoints (POST, PUT, DELETE) with authentication
- Allow public access to GET endpoints for browsing books