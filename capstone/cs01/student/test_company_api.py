from functions import AccessApi as mws
import pytest

base_url: str = "https://raw.githubusercontent.com/bclipp/"
billing_end_point: str = "APItesting/master/getBillingInfo.json"
customer_end_point: str = "APItesting/master/getCustomers.json"
site_end_point: str = "APItesting/master/getSites.json"


import pytest
import requests
from AccessApi import AccessApi

# Base URL for the API
BASE_URL = "https://raw.githubusercontent.com/cengage-ide-content/APItesting/main"

# Create AccessApi instance
api = AccessApi(BASE_URL)

# Task #01: The billing endpoint works as expected.
def test_billing_status_code():
    endpoint = "getBillingInfo.json"
    status_code = api.get_status_code(endpoint)
    assert status_code == 200, f"Expected status code 200 but got {status_code}"

def test_billing_schema():
    endpoint = "getBillingInfo.json"
    data = api.get_json_from_endpoint(endpoint)
    # Check that the keys exist and have the correct type
    assert isinstance(data, list), "Response is not a list"
    for item in data:
        assert "id" in item and isinstance(item["id"], int), "Missing or invalid 'id'"
        assert "FirstName" in item and isinstance(item["FirstName"], str), "Missing or invalid 'FirstName'"
        assert "LastName" in item and isinstance(item["LastName"], str), "Missing or invalid 'LastName'"
        assert "city" in item and isinstance(item["city"], str), "Missing or invalid 'city'"
        assert "state" in item and isinstance(item["state"], str), "Missing or invalid 'state'"
        assert "Lang" in item and isinstance(item["Lang"], str), "Missing or invalid 'Lang'"
        assert "SSN" in item and isinstance(item["SSN"], str), "Missing or invalid 'SSN'"

def test_billing_ssn_format():
    endpoint = "getBillingInfo.json"
    data = api.get_json_from_endpoint(endpoint)
    for item in data:
        ssn = item.get("SSN")
        assert len(ssn) == 11 and ssn[3] == '-' and ssn[6] == '-', f"Invalid SSN format: {ssn}"

def test_billing_response_time():
    endpoint = "getBillingInfo.json"
    response_time = api.get_response_time(endpoint)
    assert response_time < 60, f"Response time is too slow: {response_time} seconds"

# Task #02: The site endpoint works as expected.
def test_sites_status_code():
    endpoint = "getSites.json"
    status_code = api.get_status_code(endpoint)
    assert status_code == 200, f"Expected status code 200 but got {status_code}"

def test_sites_schema():
    endpoint = "getSites.json"
    data = api.get_json_from_endpoint(endpoint)
    assert isinstance(data, list), "Response is not a list"
    for item in data:
        assert "id" in item and isinstance(item["id"], int), "Missing or invalid 'id'"
        assert "address" in item and isinstance(item["address"], str), "Missing or invalid 'address'"
        assert "ThirdParty" in item and isinstance(item["ThirdParty"], str), "Missing or invalid 'ThirdParty'"
        assert "admin" in item and isinstance(item["admin"], str), "Missing or invalid 'admin'"

def test_sites_response_time():
    endpoint = "getSites.json"
    response_time = api.get_response_time(endpoint)
    assert response_time < 60, f"Response time is too slow: {response_time} seconds"

# Task #03: The customer endpoint works as expected.
def test_customers_status_code():
    endpoint = "getCustomers.json"
    status_code = api.get_status_code(endpoint)
    assert status_code == 200, f"Expected status code 200 but got {status_code}"

def test_customers_schema():
    endpoint = "getCustomers.json"
    data = api.get_json_from_endpoint(endpoint)
    assert isinstance(data, list), "Response is not a list"
    for item in data:
        assert "id" in item and isinstance(item["id"], int), "Missing or invalid 'id'"
        assert "first_name" in item and isinstance(item["first_name"], str), "Missing or invalid 'first_name'"
        assert "last_name" in item and isinstance(item["last_name"], str), "Missing or invalid 'last_name'"
        assert "email" in item and isinstance(item["email"], str), "Missing or invalid 'email'"
        assert "ip_address" in item and isinstance(item["ip_address"], str), "Missing or invalid 'ip_address'"
        assert "address" in item and isinstance(item["address"], str), "Missing or invalid 'address'"

def test_customers_response_time():
    endpoint = "getCustomers.json"
    response_time = api.get_response_time(endpoint)
    assert response_time < 60, f"Response time is too slow: {response_time} seconds"
