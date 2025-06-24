"""
/src/items/service.py

Service layer for the items application.
This module contains the business logic for managing items.
It provides functions to create, read, update, and delete items.
"""

from sqlalchemy.orm import Session
from app.items import models, schemas


def get_item(db: Session, item_id: int) -> models.Item | None:
    """Retrieve an item by its ID.

    Args:
        db (Session): Database session.
        item_id (int): ID of the item to retrieve.
    Returns:
        models.Item | None: The item if found, otherwise None.
    """
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 10) -> list[models.Item]:
    """Retrieve a list of items with pagination.

    Args:
        db (Session): Database session.
        skip (int): Number of items to skip for pagination.
        limit (int): Maximum number of items to return.
    Returns:
        list[models.Item]: A list of items.
    """
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_item(db: Session, item_in: schemas.ItemCreate) -> models.Item:
    item = models.Item(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(
    db: Session, item_id: int, item_in: schemas.ItemUpdate
) -> models.Item | None:
    item = get_item(db, item_id)
    if not item:
        return None
    for key, value in item_in.model_dump(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, item_id: int) -> bool:
    item = get_item(db, item_id)
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True
