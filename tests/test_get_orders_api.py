import allure
import requests
import data


class TestGetOrdersAPI:
    @allure.title("Test get order list endpoint")
    @allure.step("Send GET request to order API and verify response")
    def test_get_order_list(self):
        response = requests.get(data.BASE_ORDER_URL)

        assert response.status_code == 200, f'Status code is {response.status_code}'
        response_data = response.json()
        assert "orders" in response_data, f'The response is missing the "orders" key'
        orders_list = response_data["orders"]
        assert isinstance(orders_list, list), "The value for the 'orders' key is not a list"
        assert len(orders_list) > 0, "The list of orders is empty"
