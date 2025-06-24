from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_item():
    """Test creating an item."""
    response = client.post("/api/v1/items/", json={"name": "Test Item", "description": "A test item."})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert "id" in data


def test_read_items():
    """Test reading all items."""
    response = client.get("/api/v1/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_item_by_id():
    """Test reading an item by ID."""
    # Create an item first
    post = client.post("/api/v1/items/", json={"name": "ItemForRead", "description": "desc"})
    item_id = post.json()["id"]

    # Read the item by ID
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == "ItemForRead"


def test_update_item():
    """Test updating an item."""
    # Create an item first
    post = client.post("/api/v1/items/", json={"name": "ToUpdate", "description": "desc"})
    item_id = post.json()["id"]

    # Update the item
    response = client.put(f"/api/v1/items/{item_id}", json={"name": "Updated", "description": "Updated desc"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated"


def test_delete_item():
    """Test deleting an item."""
    post = client.post("/api/v1/items/", json={"name": "ToDelete", "description": "desc"})
    item_id = post.json()["id"]

    # Delete the item
    response = client.delete(f"/api/v1/items/{item_id}")
    assert response.status_code == 204

    # Verify the item is deleted
    get = client.get(f"/api/v1/items/{item_id}")
    assert get.status_code == 404
