# FastAPI REST API Starter Code
# Install required packages: pip install fastapi uvicorn python-multipart

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Book Management API",
    description="A simple REST API for managing books",
    version="1.0.0"
)

# Pydantic models for request/response
class BookBase(BaseModel):
    title: str
    author: str
    isbn: Optional[str] = None
    pages: Optional[int] = None
    year: Optional[int] = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    
    class Config:
        from_attributes = True

# In-memory storage (replace with database in Task 3)
books_db = [
    {"id": 1, "title": "The Python Tutorial", "author": "Guido van Rossum", "isbn": "978-0134853987", "pages": 280, "year": 2020},
    {"id": 2, "title": "FastAPI for Beginners", "author": "Sebastian Ramirez", "isbn": "978-1484271506", "pages": 320, "year": 2021}
]
next_id = 3

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Book Management API!"}

# TODO: Implement the following endpoints:
# GET /books - Get all books
# GET /books/{book_id} - Get a specific book
# POST /books - Create a new book
# PUT /books/{book_id} - Update a book
# DELETE /books/{book_id} - Delete a book

# Example implementation for GET /books
@app.get("/books", response_model=List[Book])
async def get_books():
    """Get all books in the database"""
    return books_db

# TODO: Complete the remaining endpoints following REST API conventions

if __name__ == "__main__":
    # Run the server with: python starter-code.py
    # Or use: uvicorn starter-code:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)