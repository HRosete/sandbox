import pytest
from api import app


@pytest.fixture
def client():
    """Provides a test client for th Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client  # Provide the test client instance to the test functions

def test_add_user(client):
    """Test adding a new user"""
    response = client.post('/users', json={"id": 1, "name": "Alice"})

    assert response.status_code == 201
    assert response.get_json == {"id": 1, "name": "Alice"}

def test_get_user(client):
    """Test retrieving an existing user"""
    # First, add a user to ensure it exists
    client.post('/users', json={"id": 2, "name": "Bob"})

    response = client.get('/users/2')

    assert response.status_code == 200
    assert response.get_json() == {"id": 2, "name": "Bob"}
    