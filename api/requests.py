import logging
import json
import allure
from curlify import to_curl
from requests import Response
from allure_commons.types import AttachmentType
import requests


def response_logging(response: Response):
    logging.info("Request: " + response.request.url)

    if response.request.body:
        # Decode the request body from bytes to a string
        request_body = response.request.body.decode('utf-8')
        logging.info("INFO Request body: " + request_body)  # Log the decoded request body

    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code: " + str(response.status_code))
    logging.info("Response: " + response.text)


def request_attaching(response: Response):
    with allure.step(f'{response.request.method} {response.request.url}'):
        curl = to_curl(response.request)
        logging.info(curl)
        logging.info(f'status code: {response.status_code}')
        allure.attach(body=curl, name='curl', attachment_type=allure.attachment_type.TEXT, extension='txt')


def response_attaching(response: Response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:  # логирование тела запроса если оно есть
        allure.attach(
            body=response.request.body.decode('utf-8') if response.request.body else None,
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )


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
