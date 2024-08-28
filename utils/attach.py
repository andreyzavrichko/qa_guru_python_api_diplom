import json
import logging

import allure
from allure_commons.types import AttachmentType
from curlify import to_curl
from requests import Response


def response_logging(response: Response):
    logging.info("Request: " + response.request.url)

    if response.request.body:
        request_body = response.request.body.decode('utf-8')
        logging.info("INFO Request body: " + request_body)

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

    if response.request.body:
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
