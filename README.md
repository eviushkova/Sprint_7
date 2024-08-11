# Scooter Service API Test Suite

## Overview

This project contains automated tests for the Scooter Service API, designed to verify the functionality of endpoints related to couriers and orders. The tests are written in Python using the `pytest` framework and utilize `allure` for generating test reports. The project aims to ensure that the API behaves as expected under various conditions.

## Structure

The test suite is divided into the following main classes:

1. **`TestCreateCourierAPI`**: Tests related to the creation of couriers.
    - `test_create_courier_success`: Verifies that a courier can be created successfully.
    - `test_create_courier_duplicate`: Ensures that attempting to create a courier with a duplicate login fails.
    - `test_create_courier_missing_required_fields`: Checks the API's response when required fields are missing.

2. **`TestLoginCourierAPI`**: Tests related to the courier login functionality.
    - `test_login_courier_success`: Validates successful login with correct credentials.
    - `test_login_courier_missing_login`: Tests the API's response when the login field is missing.
    - `test_login_courier_missing_password`: Tests the API's response when the password field is missing.
    - `test_login_courier_invalid_credentials`: Checks the API's response to invalid login credentials.
    - `test_login_courier_nonexistent_user`: Ensures the API handles login attempts with non-existent users correctly.

3. **`TestCreateOrderAPI`**: Tests related to the creation of orders.
    - `test_create_order_with_varied_color_options`: Validates order creation with different color options.

4. **`TestGetOrdersAPI`**: Tests related to retrieving the list of orders.
    - `test_get_order_list`: Verifies that the API can retrieve a list of orders correctly.

## Setup and Execution

### Prerequisites

- Python 3.11.9 or later
- `pytest` 8.2.0
- `allure-pytest` 2.13.5
- Additional dependencies as listed in `requirements.txt`

### Running Tests

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
