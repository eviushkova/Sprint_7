import allure
import requests
import data


class TestLoginCourierAPI:
    @allure.title("Successful login with valid credentials")
    @allure.step("Send POST request to login with valid credentials and verify the response")
    def test_login_courier_success(self, create_courier):
        login, password = create_courier
        response = requests.post(data.COURIER_LOGIN_URL, json={
            "login": login,
            "password": password
        })

        assert response.status_code == 200, f'Status code is {response.status_code}'
        assert response.json()["id"] is not None, f'Body={response.json()}'

    @allure.title("Login attempt with missing login field")
    @allure.step("Send POST request with missing 'login' field and verify the response")
    def test_login_courier_missing_login(self, create_courier):
        login, password = create_courier
        login_data = {
            "password": password
        }
        response = requests.post(data.COURIER_LOGIN_URL, json=login_data)

        assert response.status_code == 400, f'Status code is {response.status_code}'
        assert response.json()["message"] == "Недостаточно данных для входа", f'Body is {response.json()["message"]}'

    @allure.title("Login attempt with missing password field")
    @allure.step("Send POST request with missing 'password' field and verify the response")
    def test_login_courier_missing_password(self, create_courier):
        login, password = create_courier
        login_data = {
            "login": login
        }
        response = requests.post(data.COURIER_LOGIN_URL, json=login_data)

        assert response.status_code == 504, f'Status code is {response.status_code}'

    @allure.title("Login attempt with invalid credentials")
    @allure.step("Send POST request with invalid credentials and verify the response")
    def test_login_courier_invalid_credentials(self, create_courier):
        login, password = create_courier
        response = requests.post(data.COURIER_LOGIN_URL, json={
            "login": login,
            "password": password.upper()
        })

        assert response.status_code == 404, f'Status code is {response.status_code}'
        assert response.json()["message"] == "Учетная запись не найдена", f'Body is {response.json()["message"]}'

    @allure.title("Login attempt with nonexistent user")
    @allure.step("Send POST request with nonexistent user credentials and verify the response")
    def test_login_courier_nonexistent_user(self, create_courier):
        login, password = create_courier
        response = requests.post(data.COURIER_LOGIN_URL, json={
            "login": login.upper(),
            "password": password
        })

        assert response.status_code == 404, f'Status code is {response.status_code}'
        assert response.json()["message"] == "Учетная запись не найдена", f'Body is {response.json()["message"]}'
