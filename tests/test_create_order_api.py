import allure
import pytest
import requests

import data
from helpers import get_order_payload


class TestCreateOrderAPI:
    @allure.title("Create order with varied color options")
    @allure.step("Send POST request to create an order with color options: {color_option} and verify the response")
    @pytest.mark.parametrize("color_option", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_varied_color_options(self, color_option):
        payload = get_order_payload(color_option)
        response = requests.post(data.BASE_ORDER_URL, json=payload)

        assert response.status_code == 201, f'Status code is {response.status_code}'
        assert response.json()["track"] is not None, f'Body is {response.json()["track"]}'
