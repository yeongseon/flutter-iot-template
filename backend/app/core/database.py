"""
/src/core/database.py

Database configuration for the application.
This module sets up the SQLAlchemy engine, session, and base class for the ORM models.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration for the application
# This configuration uses SQLite for simplicity, but can be changed to any other database.
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# Create the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
