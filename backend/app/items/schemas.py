"""
/src/items/schemas.py

Schemas for the items application.
This module defines the Pydantic schemas for the items application.
It provides data validation and serialization for the API.
"""

from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    """Base schema for items.
    This schema is used for creating and updating items.
    It includes common fields like name and description.
    """

    name: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    """Schema for creating a new item.
    This schema inherits from ItemBase and is used for item creation.
    It does not add any new fields but can be extended in the future.
    """

    pass


class ItemUpdate(ItemBase):
    """Schema for updating an existing item.
    This schema inherits from ItemBase and is used for item updates.
    It does not add any new fields but can be extended in the future.
    """

    pass


class ItemRead(ItemBase):
    """Schema for reading an item.
    This schema inherits from ItemBase and includes the item ID.
    """

    id: int

    model_config = {
        "from_attributes": True  # Pydantic v2: replaces orm_mode=True
    }