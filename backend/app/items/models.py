"""
/src/items/models.py

Models for the items application.
This module defines the SQLAlchemy models for the items application.
It provides the database schema for storing items.
"""

from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base


class Item(Base):
    """Item model for the items application."""

    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
