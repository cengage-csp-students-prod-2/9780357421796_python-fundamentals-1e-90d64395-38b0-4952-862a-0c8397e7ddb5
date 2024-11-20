from functions import AccessApi as mws
import pytest

base_url: str = "https://raw.githubusercontent.com/bclipp/"
billing_end_point: str = "APItesting/master/getBillingInfo.json"
customer_end_point: str = "APItesting/master/getCustomers.json"
site_end_point: str = "APItesting/master/getSites.json"


import requests
from typing import List, Dict

class AccessApi:
    def __init__(self, base_url: str):
        """
        Constructor to initialize base URL for the API.
        :param base_url: The base URL of the API
        """
        self.base_url = base_url

    def get_base_url(self) -> str:
        """
        Returns the current base URL of the API.
        :return: The base URL
        """
        return self.base_url

    def set_base_url(self, base_url: str) -> None:
        """
        Sets the current base URL of the API.
        :param base_url: The new base URL
        """
        self.base_url = base_url

    def is_alive(self) -> bool:
        """
        Tests if the base URL is responding to GET requests.
        :return: True if the base URL is alive, False otherwise
        """
        try:
            response = requests.get(self.base_url)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def get_json(self, endpoint: str) -> List[Dict]:
        """
        Sends a GET request to the concatenated URL (base URL + endpoint) and returns the response as a list.
        :param endpoint: The endpoint to be concatenated to the base URL
        :return: The JSON response as a list
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response.json()

    def get_status_code(self, endpoint: str) -> int:
        """
        Sends a GET request to the concatenated URL (base URL + endpoint) and returns the status code.
        :param endpoint: The endpoint to be concatenated to the base URL
        :return: The HTTP status code of the response
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response.status_code

    def get_response_time(self, endpoint: str) -> float:
        """
        Sends a GET request to the concatenated URL (base URL + endpoint) and returns the response time in seconds.
        :param endpoint: The endpoint to be concatenated to the base URL
        :return: The response time in seconds
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response.elapsed.total_seconds()

# TASK 2

import pytest
from AccessApi import AccessApi

# Setup a base URL for testing
BASE_URL = "https://raw.githubusercontent.com/cengage-ide-content/APItesting/main"

@pytest.fixture
def api():
    return AccessApi(BASE_URL)

# Task #01: The billing endpoint works as expected.
def test_billing_status_code(api):
    response = api.get_status_code("getBillingInfo.json")
    assert response == 200

def test_billing_schema(api):
    json_response = api.get_json("getBillingInfo.json")
    assert isinstance(json_response, list)
    if len(json_response) > 0:
        assert "id" in json_response[0] and isinstance(json_response[0]["id"], int)
        assert "FirstName" in json_response[0] and isinstance(json_response[0]["FirstName"], str)
        assert "SSN" in json_response[0] and isinstance(json_response[0]["SSN"], str)
        assert len(json_response[0]["SSN"]) == 11  # Check if SSN is in the format XXX-XX-XXXX

def test_billing_response_time(api):
    response_time = api.get_response_time("getBillingInfo.json")
    assert response_time < 60  # Ensure the response time is less than 60 seconds.

# Task #02: The site endpoint works as expected.
def test_sites_status_code(api):
    response = api.get_status_code("getSites.json")
    assert response == 200

def test_sites_schema(api):
    json_response = api.get_json("getSites.json")
    assert isinstance(json_response, list)
    if len(json_response) > 0:
        assert "id" in json_response[0] and isinstance(json_response[0]["id"], int)
        assert "address" in json_response[0] and isinstance(json_response[0]["address"], str)
        assert "ThirdParty" in json_response[0] and isinstance(json_response[0]["ThirdParty"], str)
        assert "admin" in json_response[0] and isinstance(json_response[0]["admin"], str)

def test_sites_response_time(api):
    response_time = api.get_response_time("getSites.json")
    assert response_time < 60  # Ensure the response time is less than 60 seconds.

# Task #03: The customer endpoint works as expected.
def test_customers_status_code(api):
    response = api.get_status_code("getCustomers.json")
    assert response == 200

def test_customers_schema(api):
    json_response = api.get_json("getCustomers.json")
    assert isinstance(json_response, list)
    if len(json_response) > 0:
        assert "id" in json_response[0] and isinstance(json_response[0]["id"], int)
        assert "first_name" in json_response[0] and isinstance(json_response[0]["first_name"], str)
        assert "email" in json_response[0] and isinstance(json_response[0]["email"], str)

def test_customers_response_time(api):
    response_time = api.get_response_time("getCustomers.json")
    assert response_time < 60  # Ensure the response time is less than 60 seconds.

# Task #04: Ensure all tests pass without errors.
def test_all_endpoints(api):
    assert api.is_alive()  # Ensure the base URL is alive


    
# task 3
@pytest.mark.parametrize('base_url', [base_url])
@pytest.mark.parametrize('billing_end_point', [billing_end_point, customer_end_point, site_end_point])


@pytest.mark.parametrize('base_url', [base_url])
@pytest.mark.parametrize('billing_end_point',[billing_end_point,customer_end_point,site_end_point])
def test_billing_validate_time(base_url,billing_end_point):

