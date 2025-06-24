"""
/src/main.py
Main entry point for the FastAPI application.
This module initializes the FastAPI application, sets up the database, and includes the items router.
"""

from fastapi import FastAPI
from app.core.database import Base, engine
from app.items.router import router as item_router


# Create all tables in the database
# This will create the tables defined in the models if they do not exist.

Base.metadata.create_all(bind=engine)

# Create FastAPI application instance
app = FastAPI(
    title="FastAPI Items API",
    description="Items 도메인 기반 REST API with SQLite",
    version="1.0.0",
)

# Register the items router
app.include_router(item_router, prefix="/api/v1")


# Define a simple health check endpoint
@app.get("/hello")
def say_hello():
    return {"message": "Hello from FastAPI!"}
