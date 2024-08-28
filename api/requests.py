import allure
import requests

from utils.attach import response_logging, response_attaching, request_attaching


def get_request(url, params=None):
    with allure.step('Отправить GET запрос'):
        response = requests.get(
            url=url,
            params=params
        )
    with allure.step('Логируем response'):
        response_logging(response)
    with allure.step('Добавляем вложения'):
        response_attaching(response)

    return response


def post_request(url, json):
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    with allure.step('Отправить POST запрос'):
        response = requests.post(
            url=url,
            headers=headers,
            json=json
        )
    with allure.step('Добавляем request'):
        request_attaching(response)
    with allure.step('Логируем response'):
        response_logging(response)
    with allure.step('Добавляем вложения'):
        response_attaching(response)

    return response


def delete_request(url, params=None):
    with allure.step('Отправить DELETE запрос'):
        response = requests.delete(
            url=url,
            params=params
        )
    with allure.step('Логируем response'):
        response_logging(response)
    with allure.step('Добавляем вложения'):
        response_attaching(response)

    return response
