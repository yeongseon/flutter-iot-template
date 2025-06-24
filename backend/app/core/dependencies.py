"""
/src/core/dependencies.py

Dependencies for the core application.
This module provides dependency functions for the core application.
"""

from app.core.database import SessionLocal
from sqlalchemy.orm import Session


def get_db() -> Session:
    """Get a database session.
    This function provides a database session for use in the application.
    It yields a session object that can be used to interact with the database.
    After the session is used, it is closed to release resources.

    Returns:
        Session: A SQLAlchemy session object for database operations.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
