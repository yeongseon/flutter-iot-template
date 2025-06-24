"""
/src/items/router.py

Router for the items application.
This module defines the FastAPI routes for managing items.
It provides endpoints to create, read, update, and delete items.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.items import schemas, service

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", response_model=schemas.ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(item_in: schemas.ItemCreate, db: Session = Depends(get_db)):
    """Create a new item.

    Args:
        item_in (schemas.ItemCreate): The item data to create.
        db (Session): Database session dependency.
    Returns:
        schemas.ItemRead: The created item.
    """
    return service.create_item(db, item_in)


@router.get("/", response_model=list[schemas.ItemRead])
def list_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """List items with pagination.

    Args:
        skip (int): Number of items to skip for pagination.
        limit (int): Maximum number of items to return.
        db (Session): Database session dependency.
    Returns:
        list[schemas.ItemRead]: A list of items.
    """
    return service.get_items(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=schemas.ItemRead)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """Read an item by its ID.

    Args:
        item_id (int): ID of the item to retrieve.
        db (Session): Database session dependency.
    Returns:
        schemas.ItemRead: The retrieved item.
    Raises:
        HTTPException: If the item is not found.
    """
    item = service.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/{item_id}", response_model=schemas.ItemRead)
def update_item(
    item_id: int, item_in: schemas.ItemUpdate, db: Session = Depends(get_db)
):
    """Update an existing item.

    Args:
        item_id (int): ID of the item to update.
        item_in (schemas.ItemUpdate): The updated item data.
        db (Session): Database session dependency.
    Returns:
        schemas.ItemRead: The updated item.
    Raises:
        HTTPException: If the item is not found.
    """
    item = service.update_item(db, item_id, item_in)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Delete an item by its ID.

    Args:
        item_id (int): ID of the item to delete.
        db (Session): Database session dependency.
    Raises:
        HTTPException: If the item is not found.
    """
    success = service.delete_item(db, item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
