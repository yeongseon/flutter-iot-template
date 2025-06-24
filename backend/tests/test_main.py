from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_hello_endpoint():
    """Test the /hello endpoint."""
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI!"}


def test_get_items_redirect():
    """Test the /api/v1/items endpoint for redirection."""
    # This test checks if the /api/v1/items endpoint redirects correctly.
    # The expected status codes are 200 (OK), 307 (Temporary Redirect), or 308 (Permanent Redirect).
    response = client.get("/api/v1/items")
    assert response.status_code in (200, 307, 308)
