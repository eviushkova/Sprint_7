import random

import string

from data import BASE_ORDER_PAYLOAD


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))

    return random_string


def generate_courier_data():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return {
        "login": login,
        "password": password,
        "firstName": first_name
    }


def get_order_payload(color_options):
    payload = BASE_ORDER_PAYLOAD.copy()
    payload["color"] = color_options

    return payload
