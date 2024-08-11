import allure
import pytest
import requests
import data
from helpers import generate_courier_data


@allure.step("Setup and teardown for courier creation: create a new courier and provide credentials")
@pytest.fixture
def create_courier():
    courier_credentials = generate_courier_data()
    requests.post(data.COURIER_BASE_URL, json=courier_credentials)
    yield courier_credentials['login'], courier_credentials['password']
    login_courier = requests.post(data.COURIER_LOGIN_URL, json={
        "login": courier_credentials['login'],
        "password": courier_credentials['password']
    })
    courier_id = login_courier.json()["id"]
    requests.delete(f'{data.COURIER_BASE_URL}{courier_id}')