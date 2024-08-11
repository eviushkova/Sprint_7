import allure
import requests
import data
import pytest
from helpers import generate_courier_data


class TestCreateCourierAPI:
    @allure.title("Successfully create a new courier")
    @allure.step("Send POST request to create a courier and verify the response")
    def test_create_courier_success(self):
        courier_data = generate_courier_data()
        response = requests.post(data.COURIER_BASE_URL, json=courier_data)

        assert response.status_code == 201, f'Status code is {response.status_code}'
        assert response.json()["ok"] is True, f'Body={response.json()["ok"]}'

    @allure.title("Attempt to create courier with duplicate login")
    @allure.step(
        "Send POST request to create a courier, then send another request with the same data and verify the response")
    def test_create_courier_duplicate(self):
        courier_data = generate_courier_data()
        response_1 = requests.post(data.COURIER_BASE_URL, json=courier_data)

        assert response_1.status_code == 201, f'Status code is {response_1.status_code}'
        assert response_1.json()["ok"] is True, f'Body={response_1.json()["ok"]}'

        response_2 = requests.post(data.COURIER_BASE_URL, json=courier_data)

        assert response_2.status_code == 409, f'Status code is {response_2.status_code}'
        assert response_2.json()[
                   "message"] == "Этот логин уже используется. Попробуйте другой.", f'Body={response_2.json()["message"]}'

    @allure.title("Create courier with missing required fields")
    @allure.step("Send POST request to create a courier with missing fields and verify the response")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_fields(self, missing_field):
        courier_data = generate_courier_data()
        courier_data.pop(missing_field, None)

        response = requests.post(data.COURIER_BASE_URL, json=courier_data)

        assert response.status_code == 400, f'Status code is {response.status_code}, body={response.json()["message"]}'
        assert response.json()[
                   "message"] == "Недостаточно данных для создания учетной записи", f'Body={response.json()["message"]}'
