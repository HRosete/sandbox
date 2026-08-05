import requests

class APIClient:
    """Simulates an external API client."""

    def get_user_data(self, user_id):
        response = requests.get(f"https://api.example.com/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        raise ValueError("API request failed with status code: {}".format(response.status_code))


class UserService:
    """Uses APICLient to fetch user data and process it."""

    def __init__(self, api_client):
        self.api_client = api_client  # Dependency injection of APIClient

    def get_username(self, user_id):
        """Fetches a user and returns their username in uppercase."""

        user_data = self.api_client.get_user_data(user_id)  # Calls APICLient
        return user_data["name"].upper()  # Processes the data and returns the result

    