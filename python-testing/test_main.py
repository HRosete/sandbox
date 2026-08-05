import pytest
# from  python-testing.main import UserManager
from main import UserManager

@pytest.fixture
def user_manager():
    """Creates a fresh instance of UserManager before each test."""
    return main.UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("john_doe", "john@example.com") == True
    assert user_manager.get_user("john_doe") == "john@example.com"

def test_add_duplicate_user(user_manager):
    user_manager.add_user("john_doe", "john@example.com")

    with pytest.raises(ValueError):
        user_manager.add_user("john_doe", "another@example.com")
