"""
/src/main.py

Main entry point for the FastAPI application.
This module initializes the FastAPI application, sets up the database,
configures CORS, and includes the items router.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.items.router import router as item_router

# Create database tables from SQLAlchemy models if they do not already exist
Base.metadata.create_all(bind=engine)

# Create FastAPI application instance
app = FastAPI(
    title="FastAPI Items API",
    description="REST API for managing items with SQLite",
    version="1.0.0",
)

# Configure CORS to allow requests from frontend (e.g., Flutter Web)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace "*" with specific allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the item router under the /api/v1 path
app.include_router(item_router, prefix="/api/v1")

# Simple health check endpoint
@app.get("/hello")
def say_hello():
    return {"message": "Hello from FastAPI!"}
