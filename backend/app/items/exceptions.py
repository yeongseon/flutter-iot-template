"""
/src/items/exceptions.py

Exceptions for the items application.
This module defines custom exceptions for the items application.
It provides a way to handle specific error cases in the application.
"""

from fastapi import HTTPException, status
from app.items.constants import ITEM_NOT_FOUND


class ItemNotFoundException(HTTPException):
    """Exception raised when an item is not found."""

    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=ITEM_NOT_FOUND)
