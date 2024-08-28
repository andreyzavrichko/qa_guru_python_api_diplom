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


def post_request(url, headers, json):
    response = requests.post(
        url=url,
        headers=headers,
        json=json
    )
    request_attaching(response)
    response_logging(response)
    response_attaching(response)

    return response
