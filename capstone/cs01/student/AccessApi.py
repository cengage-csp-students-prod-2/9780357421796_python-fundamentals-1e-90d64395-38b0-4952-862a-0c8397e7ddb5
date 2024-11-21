import requests
import time
from typing import List, Dict, Any

class AccessApi:
    def __init__(self, base_url: str):
        """
        Constructor to initialize the base URL of the API
        """
        self.base_url = base_url
    
    def get_base_url(self) -> str:
        """
        Returns the base URL.
        """
        return self.base_url
    
    def set_base_url(self, base_url: str) -> None:
        """
        Sets a new base URL.
        """
        self.base_url = base_url
    
    def is_alive(self) -> bool:
        """
        Checks if the base URL is responding to GET requests.
        Returns True if it does, False otherwise.
        """
        try:
            response = requests.get(self.base_url)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False
    
    def get_json_from_endpoint(self, endpoint: str) -> List[Dict[str, Any]]:
        """
        Takes an endpoint, concatenates it with the base URL, and sends a GET request.
        Returns the response JSON as a list.
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response.json()
    
    def get_status_code(self, endpoint: str) -> int:
        """
        Takes an endpoint, concatenates it with the base URL, and returns the HTTP status code.
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response.status_code
    
    def get_response_time(self, endpoint: str) -> float:
        """
        Takes an endpoint, concatenates it with the base URL, and returns the elapsed response time.
        """
        url = f"{self.base_url}/{endpoint}"
        start_time = time.time()
        response = requests.get(url)
        elapsed_time = time.time() - start_time
        return elapsed_time




