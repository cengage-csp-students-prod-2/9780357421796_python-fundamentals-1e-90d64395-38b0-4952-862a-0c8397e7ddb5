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

# billing
def test_billing_status_code():

def test_billing_validate_schema():

def test_billing_validate_ssn():

def test_billing_validate_time():


# customers
def test_customers_status_code():

def test_customers_validate_schema():

def test_customers_validate_ssn():

def test_customers_validate_time():


# site
def test_site_status_code():

def test_site_validate_schema():

def test_site_validate_ssn():

def test_site_validate_time():

    
# task 3
@pytest.mark.parametrize('base_url', [base_url])
@pytest.mark.parametrize('billing_end_point', [billing_end_point, customer_end_point, site_end_point])


@pytest.mark.parametrize('base_url', [base_url])
@pytest.mark.parametrize('billing_end_point',[billing_end_point,customer_end_point,site_end_point])
def test_billing_validate_time(base_url,billing_end_point):

